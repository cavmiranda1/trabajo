# Generated by Django 4.1.7 on 2023-03-28 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_nacionalidad_persona_nacionalidad_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='nacionalidad_id',
            new_name='pais',
        ),
        migrations.RenameField(
            model_name='personapais',
            old_name='nacionalidad_id',
            new_name='pais',
        ),
    ]
