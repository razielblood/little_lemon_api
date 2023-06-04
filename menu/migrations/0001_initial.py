# Generated by Django 4.2.1 on 2023-06-04 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("slug", models.SlugField()),
                ("title", models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="MenuItem",
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
                ("title", models.CharField(db_index=True, max_length=255)),
                (
                    "price",
                    models.DecimalField(db_index=True, decimal_places=2, max_digits=6),
                ),
                ("featured", models.BooleanField(db_index=True)),
                (
                    "Category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="menu.category"
                    ),
                ),
            ],
        ),
    ]
