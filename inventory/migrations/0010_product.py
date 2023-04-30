# Generated by Django 4.2 on 2023-04-29 12:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0009_alter_brand_tag"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(blank=True, max_length=255)),
                ("content", models.TextField(blank=True)),
                ("quantity", models.IntegerField(default=0)),
                (
                    "time_create",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Time_created"
                    ),
                ),
                (
                    "time_update",
                    models.DateTimeField(auto_now=True, verbose_name="Time_updated"),
                ),
                (
                    "is_published",
                    models.BooleanField(default=True, verbose_name="Is_published"),
                ),
            ],
        ),
    ]