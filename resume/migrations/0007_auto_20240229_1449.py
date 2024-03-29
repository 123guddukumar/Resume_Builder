# Generated by Django 2.2.4 on 2024-02-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_resume_about'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='start_edu',
            new_name='end_grad',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='education',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='end_edu',
        ),
        migrations.AddField(
            model_name='resume',
            name='Inter',
            field=models.TextField(default='MJK college bettiah'),
        ),
        migrations.AddField(
            model_name='resume',
            name='end_inter',
            field=models.DateField(default='2024-01-01'),
        ),
        migrations.AddField(
            model_name='resume',
            name='end_ten',
            field=models.DateField(default='2024-01-01'),
        ),
        migrations.AddField(
            model_name='resume',
            name='graduation',
            field=models.TextField(default='BBSBEC'),
        ),
        migrations.AddField(
            model_name='resume',
            name='start_grad',
            field=models.DateField(default='2024-01-01'),
        ),
        migrations.AddField(
            model_name='resume',
            name='start_inter',
            field=models.DateField(default='2024-01-01'),
        ),
        migrations.AddField(
            model_name='resume',
            name='start_ten',
            field=models.DateField(default='2024-01-01'),
        ),
        migrations.AddField(
            model_name='resume',
            name='tenth',
            field=models.TextField(default='RDS'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='end_job',
            field=models.DateField(default='2024-01-01'),
        ),
    ]
