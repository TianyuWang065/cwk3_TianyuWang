# Generated by Django 4.1.7 on 2023-05-10 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("booking_num", models.CharField(max_length=255)),
                ("flight_id", models.IntegerField()),
                ("price", models.FloatField()),
                ("status", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="passenger",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("gender", models.IntegerField()),
                ("nationality", models.CharField(max_length=64)),
                ("passport", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="payment_provider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("provider_name", models.CharField(max_length=255)),
                ("user_firstName", models.CharField(max_length=255)),
                ("user_lastName", models.CharField(max_length=255)),
                ("user_password", models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name="passenger_booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "booking_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="client.booking",
                    ),
                ),
                (
                    "passenger_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="client.passenger",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="invoice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("invoice_num", models.CharField(max_length=255)),
                ("status", models.CharField(max_length=255)),
                ("data_time", models.DateTimeField()),
                ("stamp", models.CharField(max_length=255)),
                (
                    "booking_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="client.booking",
                    ),
                ),
                (
                    "payment_provider_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="client.payment_provider",
                    ),
                ),
            ],
        ),
    ]