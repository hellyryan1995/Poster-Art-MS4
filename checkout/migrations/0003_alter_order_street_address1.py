# Generated by Django 3.2.8 on 2021-10-28 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20211028_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='street_address1',
            field=models.CharField(default='', max_length=80),
        ),
    ]
