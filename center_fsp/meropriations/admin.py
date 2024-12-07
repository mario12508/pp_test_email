import django.contrib.admin

import meropriations.models


@django.contrib.admin.register(meropriations.models.Structure)
class StructureAdmin(django.contrib.admin.ModelAdmin):
    pass


@django.contrib.admin.register(meropriations.models.Tip)
class TipAdmin(django.contrib.admin.ModelAdmin):
    pass


@django.contrib.admin.register(meropriations.models.Discipline)
class DisciplineAdmin(django.contrib.admin.ModelAdmin):
    pass


@django.contrib.admin.register(meropriations.models.Result)
class ResultAdmin(django.contrib.admin.ModelAdmin):
    pass


@django.contrib.admin.register(meropriations.models.Meropriation)
class MeropriationAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        meropriations.models.Meropriation.region.field.name,
        meropriations.models.Meropriation.name.field.name,
        meropriations.models.Meropriation.status.field.name,
    )
    exclude = (
        meropriations.models.Meropriation.normal_place.field.name,
    )