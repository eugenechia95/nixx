# Generated by Django 2.1.4 on 2019-01-04 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190104_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Post date'),
        ),
    ]
