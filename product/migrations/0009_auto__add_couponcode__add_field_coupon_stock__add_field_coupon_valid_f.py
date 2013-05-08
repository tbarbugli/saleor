# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CouponCode'
        db.create_table(u'product_couponcode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('coupon', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product.Coupon'])),
            ('redeemed_on', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(default='gmr51pWx27XjIGn', max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'product', ['CouponCode'])

        # Adding field 'Coupon.stock'
        db.add_column(u'product_coupon', 'stock',
                      self.gf('django.db.models.fields.DecimalField')(default='1', max_digits=10, decimal_places=4),
                      keep_default=False)

        # Adding field 'Coupon.valid_from'
        db.add_column(u'product_coupon', 'valid_from',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Coupon.valid_until'
        db.add_column(u'product_coupon', 'valid_until',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'CouponCode'
        db.delete_table(u'product_couponcode')

        # Deleting field 'Coupon.stock'
        db.delete_column(u'product_coupon', 'stock')

        # Deleting field 'Coupon.valid_from'
        db.delete_column(u'product_coupon', 'valid_from')

        # Deleting field 'Coupon.valid_until'
        db.delete_column(u'product_coupon', 'valid_until')


    models = {
        u'product.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['product.Category']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'product.coupon': {
            'Meta': {'object_name': 'Coupon', '_ormbases': [u'product.DigitalShip']},
            u'digitalship_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['product.DigitalShip']", 'unique': 'True', 'primary_key': 'True'}),
            'stock': ('django.db.models.fields.DecimalField', [], {'default': "'1'", 'max_digits': '10', 'decimal_places': '4'}),
            'valid_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'valid_until': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'product.couponcode': {
            'Meta': {'object_name': 'CouponCode'},
            'code': ('django.db.models.fields.CharField', [], {'default': "'x3xnn5sM9PmfX2M'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'coupon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product.Coupon']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'redeemed_on': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'product.digitalship': {
            'Meta': {'object_name': 'DigitalShip', '_ormbases': [u'product.Product']},
            u'product_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['product.Product']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'product.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products'", 'to': u"orm['product.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'price': ('django_prices.models.PriceField', [], {'currency': "'USD'", 'max_digits': '12', 'decimal_places': '4'}),
            'sku': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        u'product.ship': {
            'Meta': {'object_name': 'Ship', '_ormbases': [u'product.Product']},
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'length': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            u'product_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['product.Product']", 'unique': 'True', 'primary_key': 'True'}),
            'stock': ('django.db.models.fields.DecimalField', [], {'default': "'1'", 'max_digits': '10', 'decimal_places': '4'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'})
        }
    }

    complete_apps = ['product']