# Generated by Django 3.2.21 on 2023-11-04 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityPayment',
            fields=[
                ('amount', models.IntegerField()),
                ('duedate', models.CharField(max_length=45)),
                ('add_security_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'security_payment',
                'managed': False,
            },
        ),
    ]
