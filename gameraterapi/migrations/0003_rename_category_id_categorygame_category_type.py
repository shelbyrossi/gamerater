# Generated by Django 4.0.2 on 2022-02-01 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameraterapi', '0002_rename_player_id_categorygame_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorygame',
            old_name='category_id',
            new_name='category_type',
        ),
    ]
