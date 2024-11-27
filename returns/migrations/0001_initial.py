# Generated by Django 5.0.6 on 2024-11-27 16:35

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Return",
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
                ("product_id", models.CharField(max_length=50)),
                (
                    "product_category",
                    models.CharField(
                        choices=[
                            ("Apparel", "Apparel"),
                            ("Electronics", "Electronics"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "return_reason",
                    models.CharField(
                        choices=[
                            ("Wrong Size", "Wrong Size"),
                            ("Damaged", "Damaged"),
                            ("No Longer Needed", "No Longer Needed"),
                        ],
                        max_length=50,
                    ),
                ),
                ("return_date", models.DateField()),
                ("customer_feedback", models.TextField(blank=True, null=True)),
            ],
        ),
    ]