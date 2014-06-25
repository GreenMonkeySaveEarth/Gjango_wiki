# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CounterModel'
        db.create_table('celery_test_countermodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('celery_test', ['CounterModel'])


    def backwards(self, orm):
        # Deleting model 'CounterModel'
        db.delete_table('celery_test_countermodel')


    models = {
        'celery_test.countermodel': {
            'Meta': {'object_name': 'CounterModel'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['celery_test']