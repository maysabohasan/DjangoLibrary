# Generated by Django 5.0.2 on 2024-02-22 07:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(blank=True, max_length=150, null=True)),
                ('photo_book', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('photo_author', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('retal_price_day', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('retal_period', models.IntegerField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('status', models.CharField(blank=True, choices=[('available', 'available'), ('rental', 'rental'), ('sold', 'sold')], max_length=50, null=True)),
                ('Category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='ems_app.category')),
            ],
        ),
    ]
