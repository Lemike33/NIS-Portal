# Generated by Django 4.1.5 on 2023-01-19 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(default='sport', through='news.PostCategory', to='news.category'),
        ),
    ]
