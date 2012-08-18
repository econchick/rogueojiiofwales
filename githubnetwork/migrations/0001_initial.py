# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GHUser'
        db.create_table('githubnetwork_ghuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_sync', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('acct_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('gh_login', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('blog', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('avatar_url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('public_gists', self.gf('django.db.models.fields.IntegerField')()),
            ('hireable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('followers_count', self.gf('django.db.models.fields.IntegerField')()),
            ('html_url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('gravatar_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('gh_id', self.gf('django.db.models.fields.IntegerField')()),
            ('public_repos', self.gf('django.db.models.fields.IntegerField')()),
            ('following_count', self.gf('django.db.models.fields.IntegerField')()),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('githubnetwork', ['GHUser'])

        # Adding M2M table for field following on 'GHUser'
        db.create_table('githubnetwork_ghuser_following', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_ghuser', models.ForeignKey(orm['githubnetwork.ghuser'], null=False)),
            ('to_ghuser', models.ForeignKey(orm['githubnetwork.ghuser'], null=False))
        ))
        db.create_unique('githubnetwork_ghuser_following', ['from_ghuser_id', 'to_ghuser_id'])

        # Adding model 'Repo'
        db.create_table('githubnetwork_repo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_sync', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['githubnetwork.GHUser'], unique=True)),
            ('forks', self.gf('django.db.models.fields.IntegerField')()),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('open_issues', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ssh_url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('has_downloads', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('svn_url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('has_wiki', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('html_url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('watchers', self.gf('django.db.models.fields.IntegerField')()),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('clone_url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('git_url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('mirror_url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('has_issues', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('homepage', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('private', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('gh_repo_id', self.gf('django.db.models.fields.IntegerField')()),
            ('pushed_at', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('githubnetwork', ['Repo'])


    def backwards(self, orm):
        # Deleting model 'GHUser'
        db.delete_table('githubnetwork_ghuser')

        # Removing M2M table for field following on 'GHUser'
        db.delete_table('githubnetwork_ghuser_following')

        # Deleting model 'Repo'
        db.delete_table('githubnetwork_repo')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'githubnetwork.ghuser': {
            'Meta': {'object_name': 'GHUser'},
            'acct_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'avatar_url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'bio': ('django.db.models.fields.TextField', [], {}),
            'blog': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'followers_count': ('django.db.models.fields.IntegerField', [], {}),
            'following': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'following_rel_+'", 'to': "orm['githubnetwork.GHUser']"}),
            'following_count': ('django.db.models.fields.IntegerField', [], {}),
            'gh_id': ('django.db.models.fields.IntegerField', [], {}),
            'gh_login': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gravatar_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'hireable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'html_url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_sync': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'public_gists': ('django.db.models.fields.IntegerField', [], {}),
            'public_repos': ('django.db.models.fields.IntegerField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'githubnetwork.repo': {
            'Meta': {'object_name': 'Repo'},
            'clone_url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'forks': ('django.db.models.fields.IntegerField', [], {}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gh_repo_id': ('django.db.models.fields.IntegerField', [], {}),
            'git_url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'has_downloads': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_issues': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_wiki': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'homepage': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'html_url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'last_sync': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'mirror_url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'open_issues': ('django.db.models.fields.IntegerField', [], {}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['githubnetwork.GHUser']", 'unique': 'True'}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pushed_at': ('django.db.models.fields.DateTimeField', [], {}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'ssh_url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'svn_url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'watchers': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['githubnetwork']