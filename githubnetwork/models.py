import datetime
from django.contrib.auth.signals import user_logged_in
from django.db import models
from django.contrib.auth.models import User


class BaseAPIModel(models.Model):
    last_sync = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        abstract = True

    def needs_refresh(self):
        now = datetime.datetime.now()
        return not self.complete or now - self.last_sync > datetime.timedelta(days=7)

    def refresh(self, api):
        """
        Refresh the data on this object
        """
        pass # TODO


class GHUserManager(models.Manager):
    def create_from_api(self, username, api):
        obj = self.model(complete=True, gh_login=username)
        obj.refresh(api)
        return obj


class GHUser(BaseAPIModel):
    user = models.ForeignKey(User, unique=True, null=True, blank=True)
    following = models.ManyToManyField('self', related_name='followers', blank=True)
    created_at = models.DateTimeField('date account created', blank=True, null=True )
    acct_type = models.CharField(max_length=255, blank=True)
    gh_login = models.CharField(max_length=255, unique=True)
    blog = models.URLField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    avatar_url = models.URLField(max_length=255, blank=True)
    public_gists = models.IntegerField(default=0)
    hireable = models.BooleanField(default=False)
    followers_count = models.IntegerField(default=0)
    html_url = models.URLField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    name = models.CharField(max_length=255, blank=True)
    company = models.CharField(max_length=255, blank=True)
    url = models.URLField(max_length=255, blank=True)
    gravatar_id = models.CharField(max_length=255, blank=True)
    gh_id = models.IntegerField(default=-1)
    public_repos = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    location = models.CharField(max_length=255, blank=True)
    complete = models.BooleanField(default=False)

    objects = GHUserManager()

    def __unicode__(self):
        return self.gh_login

    def _translate(self, data):
        data['acct_type'] = data.pop('type', '')
        data['bio'] = data.pop('bio') if data.get('bio') is not None else ''
        data['followers_count'] = data.pop('followers', '0')
        data['following_count'] = data.pop('following', '0')
        data['gh_login'] = data.pop('login')
        data['gh_id'] = data.pop('id', '0')
        return data

    def refresh(self, api):
        data = api.get('users/%s' % self.gh_login)
        data = self._translate(data)
        for key, value in data.items():
            setattr(self, key, value)
        self.complete = True
        self.save()
        # set followers/following
        cache = {}
        def inner(iter):
            users = []
            for shortuser in iter:
                user = cache.get(shortuser['login'], None)
                if not user:
                    try:
                        user = GHUser.objects.get(gh_login=shortuser['login'])
                    except self.DoesNotExist:
                        user = GHUser.objects.create(**self._translate(shortuser))
                users.append(user)
                cache[user.gh_login] = user
            return users
        self.followers = inner(api.get_iter('users/%s/followers' % self.gh_login))
        self.following = inner(api.get_iter('users/%s/following' % self.gh_login))
        return self


class Repo(BaseAPIModel):
    owner = models.ForeignKey(GHUser, unique=True)
    forks = models.IntegerField()
    language = models.CharField(max_length=255)
    created_at = models.DateTimeField('date repo created')
    open_issues = models.IntegerField()
    description = models.CharField(max_length=255)
    ssh_url = models.URLField(max_length=255)
    has_downloads = models.BooleanField()
    svn_url = models.URLField(max_length=255)
    has_wiki = models.BooleanField()
    html_url = models.URLField(max_length=255)
    watchers = models.IntegerField()
    size = models.IntegerField()
    full_name = models.CharField(max_length=255)
    clone_url = models.URLField(max_length=255)
    git_url = models.URLField(max_length=255)
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    mirror_url = models.URLField(max_length=255)
    has_issues = models.BooleanField()
    homepage = models.CharField(max_length=255)
    private = models.BooleanField()
    gh_repo_id = models.IntegerField()
    pushed_at = models.DateTimeField('date repo pushed')

    def __unicode__(self):
        return self.name

def update_user(request, user, **kwargs):
    try:
        ghuser = GHUser.objects.get(gh_login=user.username)
    except GHUser.DoesNotExist:
        return GHUser.objects.create_from_api(user.username, request.github)
    ghuser.user = user
    ghuser.refresh(request.github)

user_logged_in.connect(update_user)
