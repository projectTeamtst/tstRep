# Generated by Django 3.1.7 on 2021-05-06 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_trainer_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='photo',
            field=models.ImageField(default='', upload_to='trainers_photo'),
        ),
    ]
