# Generated by Django 3.0.6 on 2020-06-06 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apsi_app', '0005_auto_20200526_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
