# Generated by Django 2.2.12 on 2020-08-03 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='Users/Mamedu Mercy lee/Documents/djangogirls/blog/static/images'),
        ),
    ]
