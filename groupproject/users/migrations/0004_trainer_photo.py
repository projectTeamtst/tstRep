# Generated by Django 3.1.7 on 2021-05-06 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_trainer_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='photo',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]