# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table('todo_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('people_wants_to_meet', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('time_of_event', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('todo', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table('todo_event')


    models = {
        'todo.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'people_wants_to_meet': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'time_of_event': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['todo']