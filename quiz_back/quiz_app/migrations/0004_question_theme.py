# Generated by Django 5.0.3 on 2024-03-24 17:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0003_remove_question_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz_app.theme'),
        ),
    ]
