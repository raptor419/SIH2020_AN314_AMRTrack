# Generated by Django 2.1.1 on 2020-08-03 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathtest',
            name='district',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pathtest',
            name='state',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
