# Generated by Django 3.1 on 2021-09-30 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
