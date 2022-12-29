# Generated by Django 4.1.4 on 2022-12-29 00:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('logo', models.URLField()),
            ],
            options={
                'db_table': 'services',
            },
        ),
        migrations.CreateModel(
            name='Payment_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.FloatField(default=0.0)),
                ('paymentDate', models.DateField(auto_now_add=True)),
                ('expirationDate', models.DateField(auto_now_add=True)),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='V2.services')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usersk', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expire_Paymentsd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penalty_fee_amount', models.FloatField(default=0.0)),
                ('payment_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_user', to='V2.payment_user')),
            ],
        ),
    ]