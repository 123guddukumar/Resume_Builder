# Generated by Django 2.2.4 on 2024-02-29 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_auto_20240229_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='Inter',
            new_name='inter',
        ),
        migrations.AddField(
            model_name='resume',
            name='grad_marks',
            field=models.TextField(default='88.5'),
        ),
        migrations.AddField(
            model_name='resume',
            name='inter_marks',
            field=models.TextField(default='88.5'),
        ),
        migrations.AddField(
            model_name='resume',
            name='ten_marks',
            field=models.TextField(default='88.5'),
        ),
    ]
