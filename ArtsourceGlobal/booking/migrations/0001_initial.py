# Generated by Django 2.1.1 on 2018-10-09 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homepage', '0001_initial'),
        ('signup', '0004_auto_20181009_0836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CheckIn', models.DateField()),
                ('CheckOut', models.DateField()),
                ('totalPrice', models.IntegerField(default=0)),
                ('art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookart', to='homepage.Artwork')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artist', to='signup.UserProfile')),
                ('booking_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookingowner', to='signup.UserProfile')),
            ],
            options={
                'verbose_name_plural': 'Reservation',
            },
        ),
    ]