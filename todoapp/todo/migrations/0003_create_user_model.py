# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table('todo_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=50)),
        ))
        db.send_create_signal('todo', ['User'])

        # Adding field 'Event.user'
        db.add_column('todo_event', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['todo.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table('todo_user')

        # Deleting field 'Event.user'
        db.delete_column('todo_event', 'user_id')


    models = {
        'todo.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'people_wants_to_meet': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'time_of_event': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['todo.User']"})
        },
        'todo.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['todo']