# Generated by Django 3.2.8 on 2021-10-29 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.TextField(blank=True, null=True),
        ),
    ]
