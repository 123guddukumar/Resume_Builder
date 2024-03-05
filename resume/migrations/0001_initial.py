# Generated by Django 2.2.4 on 2024-02-28 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pic', models.ImageField(upload_to='images')),
                ('email', models.EmailField(max_length=100)),
                ('number', models.IntegerField(default=0)),
                ('address', models.TextField()),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('developer', models.TextField()),
                ('skils', models.TextField()),
                ('language', models.TextField()),
                ('hobbies', models.TextField()),
                ('summary', models.TextField()),
                ('exprience', models.TextField()),
                ('ex_date', models.DateField()),
                ('education', models.TextField()),
                ('ed_date', models.DateField()),
                ('project', models.TextField()),
                ('achievement', models.TextField()),
            ],
        ),
    ]