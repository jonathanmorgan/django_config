# Generated by Django 3.1.2 on 2022-02-02 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_config', '0003_auto_20220125_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='config_property',
            name='extra_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='config_property',
            name='extra_info_json',
            field=models.JSONField(blank=True, null=True),
        ),
    ]