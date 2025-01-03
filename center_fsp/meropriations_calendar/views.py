from datetime import timedelta

from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.utils import timezone

import meropriations.models


class Home(ListView):
    template_name = "meropriations_calendar/main.html"

    def get_queryset(self):
        queryset = meropriations.models.Meropriation.objects.all()

        queryset = queryset.filter(status=meropriations.models.Meropriation.Status.ACCEPT)

        tip = self.request.GET.get("tip")
        structure = self.request.GET.get("structure")
        gender = self.request.GET.get("gender")
        region = self.request.GET.get("region")
        event_period = self.request.GET.get("event_period")
        try:
            rows_per_page = int(self.request.GET.get("rows_per_page"))
        except:
            rows_per_page = 10
        participants_count = self.request.GET.get("participants_count")

        if rows_per_page not in [10, 25, 50, 100]:
            rows_per_page = 10

        page_number = self.request.GET.get("page", 1)

        now = timezone.now()
        if event_period == "upcoming":
            # Фильтрация ближайших мероприятий
            end_date = now + timedelta(days=3)
            queryset = queryset.filter(
                date_start__gte=now, date_end__lte=end_date
            )
        elif event_period == "this_week":
            # Фильтрация мероприятий текущей недели
            start_of_week = now - timedelta(days=now.weekday())
            end_of_week = start_of_week + timedelta(days=6)

            queryset = queryset.filter(
                date_start__gte=start_of_week, date_start__lte=end_of_week
            )
        elif event_period == "next_month":
            # Фильтрация мероприятий следующего месяца
            next_half_year_start = now
            next_half_year_end = now + timedelta(weeks=26)

            queryset = queryset.filter(
                date_start__gte=next_half_year_start,
                date_start__lte=next_half_year_end,
            )
        elif event_period == "next_quarter":
            # Фильтрация мероприятий следующего квартала
            next_quarter = timezone.now() + timedelta(weeks=13)
            queryset = queryset.filter(
                date_start__gte=timezone.now(), date_start__lte=next_quarter
            )
        elif event_period == "next_half_year":
            # Фильтрация мероприятий полугодия
            next_half_year_start = now
            next_half_year_end = now + timedelta(weeks=26)
            queryset = queryset.filter(
                date_start__gte=next_half_year_start,
                date_start__lte=next_half_year_end,
            )
        elif event_period == "none":
            pass

        if tip:
            queryset = queryset.filter(tip__name=tip)
        if gender:
            if gender == "Муж.":
                queryset = (
                    queryset.filter(text__icontains="юниоры")
                    | queryset.filter(text__icontains="мужчины")
                    | queryset.filter(text__icontains="юноши")
                    | queryset.filter(text__icontains="мальчики")
                )
            else:
                queryset = (
                    queryset.filter(text__icontains="женщины")
                    | queryset.filter(text__icontains="юниорки")
                    | queryset.filter(text__icontains="девушки")
                    | queryset.filter(text__icontains="девочки")
                )
        if structure:
            queryset = queryset.filter(structure__name=structure)

        if region:
            queryset = queryset.filter(region__name=region)

        if participants_count:
            try:
                participants_count = int(participants_count)
                queryset = queryset.filter(count=participants_count)
            except ValueError:
                pass

        paginator = Paginator(queryset, rows_per_page)
        page_obj = paginator.get_page(page_number)

        return page_obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            rows_per_page = int(self.request.GET.get("rows_per_page"))
        except:
            rows_per_page = 10
        paginator = Paginator(self.get_queryset, rows_per_page)

        context["rows_per_page_options"] = ["10", "25", "50", "100"]
        context["paginator"] = paginator
        context["page_obj"] = self.get_queryset
        context["tips"] = (
            meropriations.models.Meropriation.objects.values_list(
                "tip__name", flat=True
            )
            .distinct()
            .order_by("tip__name")
        )
        context["structures"] = (
            meropriations.models.Meropriation.objects.values_list(
                "structure__name", flat=True
            )
            .distinct()
            .order_by("structure__name")
        )
        context["regions"] = (
            meropriations.models.Meropriation.objects.values_list(
                "region__name", flat=True
            )
            .distinct()
            .order_by("region__name")
        )
        context["request"] = self.request
        return context


def event_results(request, event_id):
    meropriation = get_object_or_404(meropriations.models.Meropriation, id=event_id)

    results = meropriations.models.Result.objects.filter(meropriation=meropriation)

    if not results:
        raise Http404("Результаты для данного мероприятия не найдены.")

    return render(
        request,
        "meropriations_calendar/event_results.html",
        {"meropriation": meropriation, "results": results},
    )
