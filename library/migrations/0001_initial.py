# Generated by Django 4.1.11 on 2023-12-31 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Books",
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
                ("name", models.CharField(max_length=100)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("متاح", "متاح"),
                            ("تم بيعه", "تم بيعه"),
                            ("مستعار", "مستعار"),
                        ],
                        default="Available",
                        max_length=30,
                    ),
                ),
                ("Author", models.CharField(max_length=50)),
                ("number_pages", models.IntegerField(verbose_name=20)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
