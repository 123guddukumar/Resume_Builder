# Generated by Django 2.2.4 on 2024-03-04 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0012_auto_20240304_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='about',
            field=models.TextField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='resume',
            name='gender',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='resume',
            name='language',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='resume',
            name='skills',
            field=models.TextField(null=True),
        ),
    ]