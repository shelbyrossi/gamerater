# Generated by Django 4.0.2 on 2022-02-01 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameraterapi', '0003_rename_category_id_categorygame_category_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorygame',
            name='category_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameraterapi.category'),
        ),
    ]
