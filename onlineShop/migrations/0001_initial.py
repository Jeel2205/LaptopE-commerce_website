# Generated by Django 4.1.4 on 2022-12-22 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('pincode', models.DecimalField(decimal_places=0, max_digits=6, primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=45)),
                ('delivery_charges', models.IntegerField()),
            ],
            options={
                'db_table': 'area',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('idcity', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'city',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('idstore', models.AutoField(primary_key=True, serialize=False)),
                ('store_name', models.CharField(max_length=45)),
                ('store_email', models.CharField(max_length=45)),
                ('store_phone', models.DecimalField(decimal_places=0, max_digits=10)),
                ('store_description', models.CharField(max_length=500)),
                ('area_pincode', models.ForeignKey(db_column='area_pincode', on_delete=django.db.models.deletion.DO_NOTHING, to='onlineShop.area')),
            ],
            options={
                'db_table': 'store',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('iduser', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=45)),
                ('user_password', models.CharField(max_length=15)),
                ('user_email', models.CharField(max_length=45)),
                ('user_mobile', models.DecimalField(decimal_places=0, max_digits=10)),
                ('is_admin', models.IntegerField()),
                ('area_pincode', models.ForeignKey(db_column='area_pincode', on_delete=django.db.models.deletion.DO_NOTHING, to='onlineShop.area')),
                ('store_idstore', models.ForeignKey(db_column='store_idstore', on_delete=django.db.models.deletion.DO_NOTHING, to='onlineShop.store')),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
        ),
    ]
