# Generated by Django 3.0.6 on 2020-05-26 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apsi_app', '0004_auto_20200525_1844'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertcategory',
            options={'verbose_name_plural': 'Advert categories'},
        ),
        migrations.AlterModelOptions(
            name='advertitems',
            options={'verbose_name_plural': 'Advert items'},
        ),
        migrations.AlterModelOptions(
            name='advertstatus',
            options={'verbose_name_plural': 'Advert status'},
        ),
        migrations.AlterModelOptions(
            name='observedads',
            options={'verbose_name_plural': 'Observed ads'},
        ),
    ]
