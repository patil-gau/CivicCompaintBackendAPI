# Generated by Django 3.2.6 on 2021-09-29 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_users_adhar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='adhar',
            field=models.BigIntegerField(default=67657257262),
        ),
    ]
