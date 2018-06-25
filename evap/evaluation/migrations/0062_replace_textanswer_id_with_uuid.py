# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-03 18:31
from __future__ import unicode_literals

from django.db import migrations, models
import uuid

def fill_textanswer_uuid(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    TextAnswer = apps.get_model('evaluation', 'TextAnswer')
    for obj in TextAnswer.objects.using(db_alias).all():
        obj.uuid = uuid.uuid4()
        obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0061_editor_review_reminder_template'),
    ]

    # Based on
    # https://gist.github.com/smcoll/8bb867dc631433c01fd0

    operations = [
        migrations.AddField(
            model_name='textanswer',
            name='uuid',
            field=models.UUIDField(null=True),
        ),
        migrations.RunPython(fill_textanswer_uuid, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='textanswer',
            name='uuid',
            field=models.UUIDField(primary_key=False, default=uuid.uuid4, serialize=False, editable=False),
        ),
        # rename the old id field before deleting it at the end of the
        # migration for compatibility with the sqlite driver
        migrations.RenameField(
            model_name='textanswer',
            old_name='id',
            new_name='old_id'
        ),
        migrations.RenameField(
            model_name='textanswer',
            old_name='uuid',
            new_name='id'
        ),
        migrations.AlterField(
            model_name='textanswer',
            name='id',
            field=models.UUIDField(primary_key=True, default=uuid.uuid4, serialize=False, editable=False),
        ),
        migrations.AlterModelOptions(
            name='textanswer',
            options={'ordering': ['id'], 'verbose_name': 'text answer', 'verbose_name_plural': 'text answers'},
        ),
        migrations.RemoveField(model_name='textanswer', name='old_id'),
    ]

