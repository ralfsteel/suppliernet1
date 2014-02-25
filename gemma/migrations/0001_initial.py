# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Userprofile'
        db.create_table(u'gemma_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'gemma', ['Userprofile'])

        # Adding model 'Producers'
        db.create_table(u'gemma_producers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('zipcode', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phone', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('phones', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('fax', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=200)),
        ))
        db.send_create_signal(u'gemma', ['Producers'])

        # Adding model 'Resellers'
        db.create_table(u'gemma_resellers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('zipcode', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phone', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('phones', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('fax', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=200)),
        ))
        db.send_create_signal(u'gemma', ['Resellers'])

        # Adding M2M table for field producers on 'Resellers'
        m2m_table_name = db.shorten_name(u'gemma_resellers_producers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resellers', models.ForeignKey(orm[u'gemma.resellers'], null=False)),
            ('producers', models.ForeignKey(orm[u'gemma.producers'], null=False))
        ))
        db.create_unique(m2m_table_name, ['resellers_id', 'producers_id'])

        # Adding model 'Pricelist'
        db.create_table(u'gemma_pricelist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pricelist_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pricelist_detail', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'gemma', ['Pricelist'])

        # Adding model 'Promotional'
        db.create_table(u'gemma_promotional', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('promotional_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('promotional_detail', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'gemma', ['Promotional'])


    def backwards(self, orm):
        # Deleting model 'Userprofile'
        db.delete_table(u'gemma_userprofile')

        # Deleting model 'Producers'
        db.delete_table(u'gemma_producers')

        # Deleting model 'Resellers'
        db.delete_table(u'gemma_resellers')

        # Removing M2M table for field producers on 'Resellers'
        db.delete_table(db.shorten_name(u'gemma_resellers_producers'))

        # Deleting model 'Pricelist'
        db.delete_table(u'gemma_pricelist')

        # Deleting model 'Promotional'
        db.delete_table(u'gemma_promotional')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'gemma.pricelist': {
            'Meta': {'object_name': 'Pricelist'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pricelist_detail': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'pricelist_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'gemma.producers': {
            'Meta': {'object_name': 'Producers'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            'fax': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'phones': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'gemma.promotional': {
            'Meta': {'object_name': 'Promotional'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'promotional_detail': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'promotional_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'gemma.resellers': {
            'Meta': {'object_name': 'Resellers'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            'fax': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'phones': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'producers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['gemma.Producers']", 'symmetrical': 'False'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'gemma.userprofile': {
            'Meta': {'object_name': 'Userprofile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['gemma']