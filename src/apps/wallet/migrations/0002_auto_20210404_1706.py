# Generated by Django 3.1.2 on 2021-04-04 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planspendings',
            name='spendings',
            field=models.ManyToManyField(blank=True, to='wallet.Spending'),
        ),
    ]
