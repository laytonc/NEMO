# Generated by Django 3.2.23 on 2024-02-24 05:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("NEMO", "0060_add_impersonate_permission"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="interlock",
            unique_together=set(),
        ),
    ]