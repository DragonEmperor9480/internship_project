# Generated by Django 2.2.1 on 2023-11-22 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_id', models.CharField(max_length=20)),
                ('customer_name', models.CharField(max_length=20)),
                ('mobile_name', models.CharField(max_length=20)),
                ('serial_no', models.CharField(max_length=50)),
                ('offer', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=30)),
                ('total_amt', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='customer_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('email_id', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('mobile_no', models.CharField(max_length=50)),
                ('aadhar_no', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='finance_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finance_name', models.CharField(max_length=20)),
                ('rate_of_interest', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=20)),
                ('documents_req', models.CharField(max_length=20)),
                ('min_amt', models.CharField(max_length=50)),
                ('max_amt', models.CharField(max_length=30)),
                ('duration', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='mobile_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=20)),
                ('mobile_name', models.CharField(max_length=20)),
                ('owner_name', models.CharField(max_length=20)),
                ('series', models.CharField(max_length=50)),
                ('features', models.CharField(max_length=30)),
                ('cost', models.CharField(max_length=20)),
                ('photo', models.CharField(max_length=30)),
                ('serial_no', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=20)),
                ('mobile_name', models.CharField(max_length=20)),
                ('offer_details', models.CharField(max_length=20)),
                ('start_date', models.CharField(max_length=50)),
                ('end_date', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='sale_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('sales_id', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('mobile_no', models.CharField(max_length=50)),
                ('serial_no', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=30)),
                ('offers', models.CharField(max_length=30)),
                ('payment_method', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='shop_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('owner_name', models.CharField(max_length=20)),
                ('shop_address', models.CharField(max_length=50)),
                ('land_mark', models.CharField(max_length=30)),
                ('Contact_no', models.CharField(max_length=20)),
            ],
        ),
    ]
