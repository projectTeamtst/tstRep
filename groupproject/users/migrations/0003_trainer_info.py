# Generated by Django 3.1.7 on 2021-04-23 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210412_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='info',
            field=models.TextField(default=''),
        ),
    ]
