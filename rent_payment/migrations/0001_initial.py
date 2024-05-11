# Generated by Django 3.2.21 on 2023-11-04 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RentPayment',
            fields=[
                ('due_date', models.DateField(db_column='due date')),
                ('add_rent_id', models.AutoField(primary_key=True, serialize=False)),
                ('rent_amount', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'rent_payment',
                'managed': False,
            },
        ),
    ]