# Generated by Django 4.1.4 on 2022-12-23 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineShop', '0003_user_user_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_mobile',
            field=models.CharField(max_length=10),
        ),
    ]
