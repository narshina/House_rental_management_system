# Generated by Django 3.2.21 on 2023-11-04 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('house_id', models.AutoField(primary_key=True, serialize=False)),
                ('house_name', models.CharField(max_length=45)),
                ('owner_name', models.CharField(max_length=45)),
                ('location', models.CharField(max_length=45)),
                ('district', models.CharField(max_length=45)),
                ('landmark', models.CharField(max_length=100)),
                ('number_of_bedrooms', models.CharField(max_length=45)),
                ('area_of_house', models.CharField(max_length=45)),
                ('image1', models.CharField(max_length=200)),
                ('image2', models.CharField(max_length=200)),
                ('security_payment', models.CharField(max_length=45)),
                ('rent_amount', models.CharField(max_length=45)),
                ('status', models.CharField(max_length=45)),
                ('contact_no', models.CharField(max_length=45)),
                ('block', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'property',
                'managed': False,
            },
        ),
    ]
