# Generated by Django 3.0.7 on 2020-08-23 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='vote',
            field=models.IntegerField(null=True),
        ),
    ]
