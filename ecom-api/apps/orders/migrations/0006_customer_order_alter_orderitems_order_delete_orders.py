# Generated by Django 4.1.2 on 2023-12-07 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("orders", "0005_alter_orderitems_table_alter_orders_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("isActive", models.BooleanField(default=True)),
                ("isDeleted", models.BooleanField(default=False)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified_on", models.DateTimeField(auto_now=True)),
                ("first_name", models.CharField(max_length=250)),
                ("last_name", models.CharField(max_length=250)),
                (
                    "email",
                    models.EmailField(max_length=255, verbose_name="email address"),
                ),
                ("phone", models.PositiveIntegerField()),
                ("address", models.CharField(max_length=250)),
                ("city", models.CharField(max_length=250)),
                ("zip_code", models.PositiveIntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Order",
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
                ("isActive", models.BooleanField(default=True)),
                ("isDeleted", models.BooleanField(default=False)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified_on", models.DateTimeField(auto_now=True)),
                ("paid_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orders.customer",
                    ),
                ),
            ],
            options={
                "db_table": "order",
                "ordering": ("-created_on",),
            },
        ),
        migrations.AlterField(
            model_name="orderitems",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="orders.order"
            ),
        ),
        migrations.DeleteModel(
            name="Orders",
        ),
    ]