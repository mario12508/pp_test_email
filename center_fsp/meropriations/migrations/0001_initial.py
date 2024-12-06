# Generated by Django 4.2.16 on 2024-11-23 23:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            name="Group",
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
                "verbose_name": "наименование спортивного мероприятия",
                "verbose_name_plural": "наименования спортивного мероприятия",
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
            name="Profile",
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
                ("group_request", models.CharField(max_length=150, null=True)),
                ("tip_request", models.CharField(max_length=150, null=True)),
                ("structure_request", models.CharField(max_length=150, null=True)),
                ("gender_request", models.CharField(max_length=150, null=True)),
                ("tip", models.CharField(max_length=150, null=True)),
                ("group", models.CharField(max_length=150, null=True)),
                ("structure", models.CharField(max_length=150, null=True)),
                ("gender", models.CharField(max_length=150, null=True)),
                ("place", models.CharField(max_length=150, null=True)),
                ("disciple", models.CharField(max_length=150, null=True)),
                ("event_period", models.CharField(max_length=150, null=True)),
                ("rows_per_page", models.CharField(max_length=150, null=True)),
                ("participants_count", models.CharField(max_length=150, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "дисциплина",
                "verbose_name_plural": "дисциплины",
                "ordering": ("id",),
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
                    "slug",
                    models.SlugField(max_length=200, null=True, verbose_name="слаг"),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=150, null=True, verbose_name="название"
                    ),
                ),
                ("text", models.TextField(null=True, verbose_name="текст")),
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
                    "group",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="catalog_items",
                        to="meropriations.group",
                        verbose_name="категория",
                    ),
                ),
                (
                    "structure",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="catalog_items",
                        to="meropriations.structure",
                        verbose_name="категория",
                    ),
                ),
                (
                    "tip",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="catalog_items",
                        to="meropriations.tip",
                        verbose_name="категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "мероприятие",
                "verbose_name_plural": "мероприятия",
                "ordering": ("name",),
            },
        ),
    ]