# Generated by Django 3.2.20 on 2023-09-14 01:54

from django.db import migrations

from NEMO.migrations_utils import create_news_for_version


class Migration(migrations.Migration):
    dependencies = [
        ("NEMO", "0056_version_5_2_0"),
    ]

    def new_version_news(apps, schema_editor):
        create_news_for_version(apps, "5.3.0")

    operations = [
        migrations.RunPython(new_version_news),
    ]
