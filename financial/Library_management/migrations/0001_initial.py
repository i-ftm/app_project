# Generated by Django 5.1 on 2024-08-31 20:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="book",
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
                ("titel", models.CharField(max_length=250)),
                ("price", models.DecimalField(decimal_places=3, max_digits=10)),
                (
                    "author",
                    models.CharField(max_length=100, verbose_name="author name"),
                ),
                ("publicationdate", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="user",
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
                ("name", models.CharField(max_length=100, verbose_name="user name")),
                (
                    "email",
                    models.EmailField(max_length=254, verbose_name="email address"),
                ),
                ("password", models.CharField(max_length=100)),
            ],
        ),
    ]
