# Generated by Django 3.2.7 on 2021-09-04 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediasite', '0003_remove_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
