# Generated by Django 3.2.5 on 2021-07-19 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=280)),
                ('image1', models.ImageField(blank=True, upload_to='')),
                ('image2', models.ImageField(blank=True, upload_to='')),
                ('image3', models.ImageField(blank=True, upload_to='')),
                ('image4', models.ImageField(blank=True, upload_to='')),
                ('image5', models.ImageField(blank=True, upload_to='')),
                ('image6', models.ImageField(blank=True, upload_to='')),
                ('image7', models.ImageField(blank=True, upload_to='')),
                ('image8', models.ImageField(blank=True, upload_to='')),
                ('image9', models.ImageField(blank=True, upload_to='')),
                ('image10', models.ImageField(blank=True, upload_to='')),
                ('is_public', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
