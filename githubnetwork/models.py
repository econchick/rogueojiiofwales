# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class GHUser(models.Model):
    user = models.ForeignKey(User, unique=True, verbose_name='ghuser')
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

class Repo(models.Model):
    owner = models.ForeignKey(GHUser, unique=True, verbose_name='ghuser')
    forks = models.IntegerField()
    language = models.CharField(max_length=255)
    created_at = models.DateTimeField('date repo created')
    open_issues = models.IntegerField()
    description = models.CharField(max_length=255)
    ssh_url = models.URLfield(max_length=255)
    has_downloads = models.BooleanField()
    svn_url = models.URLfield(max_length=255)
    has_wiki = models.BooleanField
    html_url = models.URLfield(max_length=255)
    watchers = models.IntegerField()
    size = models.IntegerField()
    full_name = models.CharField(max_length=255)
    clone_url = models.URLfield(max_length=255)
    git_url = models.URLfield(max_length=255)
    name = models.CharField(max_length=255)
    url = models.URLfield(max_length=255)
    mirror_url = models.URLfield(max_length=255)
    has_issues = models.BooleanField()
    homepage = models.CharField(max_length=255)
    private = models.BooleanField()
    gh_repo_id = models.IntegerField()
    pushed_at = models.DateTimeField('date repo pushed')

    def __unicode__(self):
    	return self.name
