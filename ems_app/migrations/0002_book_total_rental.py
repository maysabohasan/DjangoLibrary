# Generated by Django 5.0.2 on 2024-03-03 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_rental',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
