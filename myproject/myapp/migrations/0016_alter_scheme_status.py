# Generated by Django 5.2 on 2025-04-13 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0015_scheme"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scheme",
            name="status",
            field=models.CharField(
                choices=[("draft", "сдана"), ("approved", "не сдана")],
                default="draft",
                help_text="Текущий статус схемы",
                max_length=10,
                verbose_name="Статус",
            ),
        ),
    ]
