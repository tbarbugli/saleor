# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ExternalUserData'
        db.create_table(u'registration_externaluserdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='external_ids', to=orm['auth.User'])),
            ('service', self.gf('django.db.models.fields.TextField')(db_index=True)),
            ('username', self.gf('django.db.models.fields.TextField')(db_index=True)),
        ))
        db.send_create_signal(u'registration', ['ExternalUserData'])

        # Adding unique constraint on 'ExternalUserData', fields ['service', 'username']
        db.create_unique(u'registration_externaluserdata', ['service', 'username'])

        # Adding model 'EmailConfirmationRequest'
        db.create_table(u'registration_emailconfirmationrequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('token', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
            ('valid_until', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 6, 5, 0, 0))),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'registration', ['EmailConfirmationRequest'])

        # Adding model 'EmailChangeRequest'
        db.create_table(u'registration_emailchangerequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('token', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
            ('valid_until', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 6, 5, 0, 0))),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='email_change_requests', to=orm['auth.User'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'registration', ['EmailChangeRequest'])


    def backwards(self, orm):
        # Removing unique constraint on 'ExternalUserData', fields ['service', 'username']
        db.delete_unique(u'registration_externaluserdata', ['service', 'username'])

        # Deleting model 'ExternalUserData'
        db.delete_table(u'registration_externaluserdata')

        # Deleting model 'EmailConfirmationRequest'
        db.delete_table(u'registration_emailconfirmationrequest')

        # Deleting model 'EmailChangeRequest'
        db.delete_table(u'registration_emailchangerequest')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'registration.emailchangerequest': {
            'Meta': {'object_name': 'EmailChangeRequest'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'email_change_requests'", 'to': u"orm['auth.User']"}),
            'valid_until': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 5, 0, 0)'})
        },
        u'registration.emailconfirmationrequest': {
            'Meta': {'object_name': 'EmailConfirmationRequest'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'valid_until': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 5, 0, 0)'})
        },
        u'registration.externaluserdata': {
            'Meta': {'unique_together': "[['service', 'username']]", 'object_name': 'ExternalUserData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'external_ids'", 'to': u"orm['auth.User']"}),
            'username': ('django.db.models.fields.TextField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['registration']