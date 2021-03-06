# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sample.url'
        db.add_column(u'oj_sample', 'url',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sample.url'
        db.delete_column(u'oj_sample', 'url')


    models = {
        u'oj.quiz': {
            'Meta': {'object_name': 'Quiz'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pre_code': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            'test_code': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'oj.sample': {
            'Meta': {'object_name': 'Sample'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['oj']