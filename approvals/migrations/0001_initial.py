# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Approval'
        db.create_table('approvals_approval', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('approved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('article_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('approvals', ['Approval'])


    def backwards(self, orm):
        # Deleting model 'Approval'
        db.delete_table('approvals_approval')


    models = {
        'approvals.approval': {
            'Meta': {'object_name': 'Approval'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'article_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['approvals']