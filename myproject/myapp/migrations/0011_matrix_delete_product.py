# Generated by Django 5.2 on 2025-04-11 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0010_alter_educationalprogram_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Matrix",
            fields=[
                (
                    "id_matrix",
                    models.AutoField(
                        help_text="Уникальный идентификатор матрицы",
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID Матрицы",
                    ),
                ),
                (
                    "add_date",
                    models.DateField(
                        auto_now_add=True,
                        help_text="Дата добавления руководителем программы",
                        verbose_name="Дата добавления РОП",
                    ),
                ),
                (
                    "check_date",
                    models.DateField(
                        blank=True,
                        help_text="Дата проверки отделом лицензирования",
                        null=True,
                        verbose_name="Дата проверки ОЛ",
                    ),
                ),
                (
                    "document_link",
                    models.URLField(
                        blank=True,
                        help_text="Ссылка на документ матрицы",
                        max_length=500,
                        verbose_name="Ссылка на документ",
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True,
                        help_text="Комментарий сотрудника отдела лицензирования",
                        verbose_name="Комментарий ОЛ",
                    ),
                ),
                (
                    "assessment",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        choices=[
                            (1, "Неудовлетворительно"),
                            (2, "Удовлетворительно"),
                            (3, "Хорошо"),
                            (4, "Отлично"),
                            (5, "Превосходно"),
                        ],
                        help_text="Оценка матрицы от 1 до 5",
                        null=True,
                        verbose_name="Оценка",
                    ),
                ),
                (
                    "educational_program",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="matrices",
                        to="myapp.educationalprogram",
                        verbose_name="Образовательная программа",
                    ),
                ),
                (
                    "licensing_employee",
                    models.ForeignKey(
                        blank=True,
                        help_text="Сотрудник отдела лицензирования",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="myapp.employee",
                        verbose_name="Сотрудник ОЛ",
                    ),
                ),
            ],
            options={
                "verbose_name": "Матрица компетенций",
                "verbose_name_plural": "Матрицы компетенций",
                "db_table": "matrices",
                "ordering": ["-add_date"],
            },
        ),
        migrations.DeleteModel(
            name="Product",
        ),
    ]
