# Generated by Django 5.2 on 2025-04-11 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0006_news"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("surname", models.CharField(max_length=50, verbose_name="Фамилия")),
                ("name", models.CharField(max_length=50, verbose_name="Имя")),
                (
                    "patronymic",
                    models.CharField(max_length=50, verbose_name="Отчество"),
                ),
                (
                    "position",
                    models.CharField(max_length=100, verbose_name="Должность"),
                ),
            ],
            options={
                "verbose_name": "Сотрудник отдела лицензирования",
                "verbose_name_plural": "Сотрудники отдела лицензирования",
            },
        ),
    ]
