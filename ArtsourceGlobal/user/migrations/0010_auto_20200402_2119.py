# Generated by Django 2.2.4 on 2020-04-02 10:19

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20200326_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, max_length=8)),
                ('age', models.IntegerField(blank=True)),
                ('street1', models.CharField(blank=True, max_length=512)),
                ('street2', models.CharField(blank=True, max_length=512)),
                ('suburb', models.CharField(blank=True, max_length=128)),
                ('state', models.CharField(blank=True, max_length=128)),
                ('postalCode', models.CharField(blank=True, max_length=128)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('phone', models.CharField(blank=True, max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('painting', models.BooleanField(default=False)),
                ('sculpture', models.BooleanField(default=False)),
                ('photography', models.BooleanField(default=False)),
                ('calligraphy', models.BooleanField(default=False)),
                ('printmaking', models.BooleanField(default=False)),
                ('artsAndCrafts', models.BooleanField(default=False)),
                ('sealCutting', models.BooleanField(default=False)),
                ('artDesign', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['id'], 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AddField(
            model_name='user',
            name='refEmail',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 21, 19, 54, 910514), verbose_name='sendTime'),
        ),
        migrations.AlterField(
            model_name='user',
            name='artist',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='additionalInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.AdditionalInfo'),
        ),
        migrations.AddField(
            model_name='user',
            name='interest',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Interest'),
        ),
    ]