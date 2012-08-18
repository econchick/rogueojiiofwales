from django.db import models
from django.contrib.auth.models import User

class GHUser(models.Model):
    user = models.ForeignKey(User, unique=True)
    following = models.ManyToMany(self, related_name='followers')
    created_at = models.DateTimeField('date account created')
    acct_type = models.CharField(max_length=255)
    gh_login = models.CharField(max_length=255)
    blog = models.URLfield(max_length=255)
    email = models.EmailField(max_length=255)
    avatar_url = models.URLfield(max_length=255)
    public_gists = models.IntegerField()
    hireable = models.BooleanField()
    followers_count = models.IntegerField()
    html_url = models.URLfield(max_length=255)
    bio = models.TextField()
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    url = models.URLfield(max_length=255)
    gravatar_id = models.CharField(max_length=255)
    gh_id = models.IntegerField()
    public_repos = models.IntegerField()
    following_count = models.IntegerField()
    location = models.CharField(max_length=255)

    def __unicode__(self):
	    return self.login