# Generated by Django 5.0.6 on 2024-06-02 16:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_alter_post_publish_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 2, 16, 46, 42, 132514, tzinfo=datetime.timezone.utc)),
        ),
    ]