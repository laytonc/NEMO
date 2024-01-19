# Generated by Django 3.2.22 on 2024-01-19 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NEMO', '0058_reservation_confirmation_override_prefs'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='_pre_usage_questions',
            field=models.TextField(blank=True, db_column='pre_usage_questions', help_text='Before using a tool, questions can be asked. This field will only accept JSON format', null=True),
        ),
        migrations.AddField(
            model_name='usageevent',
            name='pre_run_data',
            field=models.TextField(blank=True, null=True),
        ),
    ]
