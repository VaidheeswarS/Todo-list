# Generated by Django 5.0.6 on 2024-06-29 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_works_submit_time_works_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
    ]
