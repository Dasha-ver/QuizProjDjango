# Generated by Django 5.0.3 on 2024-03-24 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0002_alter_question_question_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='theme',
        ),
    ]
