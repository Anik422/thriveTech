# Generated by Django 4.0.5 on 2022-07-20 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='running',
            field=models.BooleanField(default=False),
        ),
    ]
