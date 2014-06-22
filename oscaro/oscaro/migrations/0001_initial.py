# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Var'
        db.create_table(u'oscaro_var', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'oscaro', ['Var'])


    def backwards(self, orm):
        # Deleting model 'Var'
        db.delete_table(u'oscaro_var')


    models = {
        u'oscaro.var': {
            'Meta': {'object_name': 'Var'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['oscaro']