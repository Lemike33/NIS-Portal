# Generated by Django 4.1.5 on 2023-01-10 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_post_select'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rating_post',
            field=models.IntegerField(default=1),
        ),
    ]
