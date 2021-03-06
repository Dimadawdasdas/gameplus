# Generated by Django 3.2.9 on 2021-12-06 18:38

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=11)),
                ('access_level', models.CharField(choices=[('a', 'Админ'), ('m', 'Мастер'), ('c', 'Клиент')], max_length=1)),
                ('email', models.CharField(max_length=30)),
                ('login', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('reg_date', models.DateTimeField(default=datetime.datetime(2021, 12, 6, 18, 38, 47, 18935, tzinfo=utc))),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='static/images/users')),
            ],
            options={
                'ordering': ['-reg_date'],
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
                ('rate', models.CharField(max_length=10)),
                ('rules', models.TextField(default=' ')),
                ('release_date', models.DateField(default=datetime.datetime(2021, 12, 6, 18, 38, 47, 17939, tzinfo=utc))),
                ('site', models.CharField(max_length=63)),
                ('number_of_rules', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('development_budget', models.DecimalField(decimal_places=2, max_digits=12)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='static/images/games')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TechnicalTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default=' ')),
                ('complete', models.BooleanField(default=False)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameplusapp.employee')),
            ],
            options={
                'ordering': ['employee_id'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.CharField(max_length=200)),
                ('public_date', models.DateTimeField(default=datetime.datetime(2021, 12, 6, 18, 38, 47, 18935, tzinfo=utc))),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameplusapp.employee')),
            ],
            options={
                'ordering': ['-public_date'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.TextField(default=' ')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2021, 12, 6, 18, 38, 47, 20930, tzinfo=utc))),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameplusapp.chat')),
                ('sender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameplusapp.employee')),
            ],
            options={
                'ordering': ['pub_date'],
            },
        ),
        migrations.CreateModel(
            name='GameDevelopmentStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.datetime(2021, 12, 6, 18, 38, 47, 17939, tzinfo=utc))),
                ('end_date', models.DateField(default=datetime.datetime(2021, 12, 6, 18, 38, 47, 17939, tzinfo=utc))),
                ('stage_description', models.TextField(default=' ')),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameplusapp.game')),
            ],
            options={
                'ordering': ['game_id'],
            },
        ),
        migrations.CreateModel(
            name='ContractOfDevelopment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conclusion_date', models.DateField(default=datetime.datetime(2021, 12, 6, 18, 38, 47, 19933, tzinfo=utc))),
                ('contract_end_date', models.DateField(default=datetime.datetime(2021, 12, 6, 18, 38, 47, 19933, tzinfo=utc))),
                ('development_full_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_id', to='gameplusapp.employee')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_id', to='gameplusapp.employee')),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameplusapp.game')),
            ],
            options={
                'ordering': ['game_id'],
            },
        ),
        migrations.AddField(
            model_name='chat',
            name='members',
            field=models.ManyToManyField(to='gameplusapp.Employee'),
        ),
    ]
