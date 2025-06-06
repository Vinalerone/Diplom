# Generated by Django 5.2 on 2025-04-11 18:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0013_alter_matrix_licensing_employee"),
    ]

    operations = [
        migrations.AlterField(
            model_name="matrix",
            name="assessment",
            field=models.PositiveSmallIntegerField(
                blank=True,
                choices=[(1, "сдан"), (2, "не сдан")],
                null=True,
                verbose_name="Оценка",
            ),
        ),
        migrations.CreateModel(
            name="Passport",
            fields=[
                (
                    "id_matrix",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="ID Паспорта"
                    ),
                ),
                (
                    "add_date",
                    models.DateField(
                        auto_now_add=True, verbose_name="Дата добавления РОП"
                    ),
                ),
                (
                    "check_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата проверки ОЛ"
                    ),
                ),
                (
                    "document_link",
                    models.URLField(
                        blank=True, max_length=500, verbose_name="Ссылка на документ"
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True, max_length=1000, verbose_name="Комментарий ОЛ"
                    ),
                ),
                (
                    "assessment",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        choices=[(1, "сдан"), (2, "не сдан")],
                        null=True,
                        verbose_name="Оценка",
                    ),
                ),
                (
                    "educational_program",
                    models.ForeignKey(
                        help_text="Выберите образовательную программу из списка",
                        limit_choices_to={"status": "development"},
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="passports",
                        to="myapp.educationalprogram",
                        verbose_name="Образовательная программа",
                    ),
                ),
                (
                    "licensing_employee",
                    models.ForeignKey(
                        blank=True,
                        help_text="Выберите сотрудника отдела лицензирования",
                        limit_choices_to={"position__icontains": "лицензирования"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="myapp.employee",
                        verbose_name="Сотрудник ОЛ",
                    ),
                ),
            ],
            options={
                "verbose_name": "Паспорт компетенций",
                "verbose_name_plural": "Паспорта компетенций",
                "ordering": ["-add_date"],
            },
        ),
    ]
