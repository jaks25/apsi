# Generated by Django 3.0.6 on 2020-05-25 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apsi_app', '0003_auto_20200525_1839'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertcategory',
            options={'verbose_name_plural': 'AdvertCategories'},
        ),
        migrations.AlterModelOptions(
            name='advertitems',
            options={'verbose_name_plural': 'AdvertItems'},
        ),
        migrations.AlterModelOptions(
            name='advertstatus',
            options={'verbose_name_plural': 'AdvertStatus'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Counties'},
        ),
        migrations.AlterModelOptions(
            name='observedads',
            options={'verbose_name_plural': 'ObservedAds'},
        ),
    ]
