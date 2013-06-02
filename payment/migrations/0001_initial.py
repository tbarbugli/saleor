# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Payment'
        db.create_table(u'payment_payment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('variant', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('status', self.gf('django.db.models.fields.CharField')(default='waiting', max_length=10)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('transaction_id', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('total', self.gf('django.db.models.fields.DecimalField')(default='0.0', max_digits=9, decimal_places=2)),
            ('delivery', self.gf('django.db.models.fields.DecimalField')(default='0.0', max_digits=9, decimal_places=2)),
            ('tax', self.gf('django.db.models.fields.DecimalField')(default='0.0', max_digits=9, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('billing_first_name', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('billing_last_name', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('billing_address_1', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('billing_address_2', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('billing_city', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('billing_postcode', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('billing_country_code', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('billing_country_area', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('extra_data', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('token', self.gf('django.db.models.fields.CharField')(default='', max_length=36, blank=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(related_name='payments', to=orm['order.Order'])),
        ))
        db.send_create_signal(u'payment', ['Payment'])


    def backwards(self, orm):
        # Deleting model 'Payment'
        db.delete_table(u'payment_payment')


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
        u'order.order': {
            'Meta': {'ordering': "('-last_status_change',)", 'object_name': 'Order'},
            'anonymous_user_email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '75', 'blank': 'True'}),
            'billing_address': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['userprofile.Address']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_status_change': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '32'}),
            'token': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '36', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'orders'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'payment.payment': {
            'Meta': {'object_name': 'Payment'},
            'billing_address_1': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'billing_address_2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'billing_city': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'billing_country_area': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'billing_country_code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'billing_first_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'billing_last_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'billing_postcode': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'delivery': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '9', 'decimal_places': '2'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'extra_data': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'payments'", 'to': u"orm['order.Order']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'waiting'", 'max_length': '10'}),
            'tax': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '9', 'decimal_places': '2'}),
            'token': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '36', 'blank': 'True'}),
            'total': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '9', 'decimal_places': '2'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'variant': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'userprofile.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'country_area': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'street_address_1': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'street_address_2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        }
    }

    complete_apps = ['payment']