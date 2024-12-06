# Generated by Django 4.2.16 on 2024-12-06 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Discipline",
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
                (
                    "name",
                    models.CharField(
                        max_length=150, unique=True, verbose_name="название"
                    ),
                ),
            ],
            options={
                "verbose_name": "дисциплина",
                "verbose_name_plural": "дисциплины",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Meropriation",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("consideration", "Consideration"),
                            ("acceptance", "Accept"),
                        ],
                        default="consideration",
                        max_length=30,
                        verbose_name="статус мероприятия",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=150, null=True, verbose_name="название"
                    ),
                ),
                (
                    "text",
                    models.TextField(null=True, verbose_name="описание мероприятия"),
                ),
                (
                    "count",
                    models.PositiveIntegerField(
                        null=True, verbose_name="количество участников"
                    ),
                ),
                ("place", models.TextField(null=True, verbose_name="место проведения")),
                (
                    "normal_place",
                    models.TextField(
                        null=True, verbose_name="нормальное место проведения"
                    ),
                ),
                ("disciplines", models.TextField(null=True, verbose_name="дисциплины")),
                ("date_start", models.DateField(null=True, verbose_name="дата начала")),
                ("date_end", models.DateField(null=True, verbose_name="дата конца")),
                (
                    "region",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="meropriation_regions",
                        to="users.region",
                        verbose_name="регион",
                    ),
                ),
            ],
            options={
                "verbose_name": "мероприятие",
                "verbose_name_plural": "мероприятия",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Structure",
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
                (
                    "name",
                    models.CharField(
                        max_length=150, unique=True, verbose_name="название"
                    ),
                ),
            ],
            options={
                "verbose_name": "состав",
                "verbose_name_plural": "составы",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Tip",
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
                (
                    "name",
                    models.CharField(
                        max_length=150, unique=True, verbose_name="название"
                    ),
                ),
            ],
            options={
                "verbose_name": "тип соревнования",
                "verbose_name_plural": "типы соревнований",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Result",
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
                (
                    "meropriation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="meropriations.meropriation",
                        verbose_name="мероприятие",
                    ),
                ),
            ],
            options={
                "verbose_name": "результат",
                "verbose_name_plural": "результаты",
            },
        ),
        migrations.AddField(
            model_name="meropriation",
            name="structure",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="meropriation_structures",
                to="meropriations.structure",
                verbose_name="состав",
            ),
        ),
        migrations.AddField(
            model_name="meropriation",
            name="tip",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="meropriation_tips",
                to="meropriations.tip",
                verbose_name="тип соревнования",
            ),
        ),
    ]
