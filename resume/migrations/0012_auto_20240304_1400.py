# Generated by Django 2.2.4 on 2024-03-04 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0011_auto_20240304_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='achievement1',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='achievement2',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='position1',
            field=models.CharField(default='Gold', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='position2',
            field=models.CharField(default='Gold', max_length=20, null=True),
        ),
    ]
