# Generated by Django 3.1.2 on 2021-03-22 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20210321_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('work_started', models.BooleanField(default=False, verbose_name='Work started')),
                ('work_done', models.BooleanField(default=False, verbose_name='Work done')),
                ('target_hours', models.PositiveIntegerField(default=0, help_text='Maximum target hours is 99', verbose_name='Target hours needed')),
                ('time_left', models.TimeField(blank=True, null=True, verbose_name='Time left')),
                ('is_achieved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_spent', models.TimeField(blank=True, null=True, verbose_name='Time spent')),
                ('date', models.DateField(blank=True, null=True)),
                ('goal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='works', to='goals.goal')),
            ],
        ),
    ]
