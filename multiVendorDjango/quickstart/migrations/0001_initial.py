# Generated by Django 3.0.1 on 2020-08-23 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=50)),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('password', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'customers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('product_id', models.CharField(max_length=50)),
                ('image_url', models.CharField(max_length=200)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'gallery',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('vendor_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=250)),
                ('long_description', models.TextField()),
                ('in_stocks', models.IntegerField()),
                ('type', models.IntegerField()),
                ('sales_price', models.CharField(max_length=10)),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('updated_by', models.CharField(max_length=50)),
                ('short_description', models.CharField(max_length=100)),
                ('parent_id', models.CharField(max_length=50)),
                ('category', models.IntegerField()),
                ('sub_category', models.IntegerField()),
                ('max_quantity_per_order', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('backorders_allowed', models.IntegerField()),
                ('regular_price', models.CharField(max_length=10)),
                ('tag', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('id_proof', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('category', models.IntegerField()),
            ],
            options={
                'db_table': 'vendors',
                'managed': False,
            },
        ),
    ]
