# Generated by Django 3.2.5 on 2021-08-02 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snscontrol', '0006_auto_20210720_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=280),
        ),
    ]
