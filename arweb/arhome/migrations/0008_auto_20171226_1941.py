# Generated by Django 2.0 on 2017-12-26 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhome', '0007_auto_20171224_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='videos_subscribe',
            field=models.ManyToManyField(to='arhome.Videos'),
        ),
    ]
