from django.utils.datetime_safe import datetime
from drf_haystack.filters import HaystackFilter
from rest_framework.filters import BaseFilterBackend
# from haystack.utils.geo import Point, D
# from constance import config


class IsMaleFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(is_male=True)


class IsFemaleFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(is_female=True)


class IsDhakaFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(is_dhaka=True)


class IsKhulnaFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(is_khulna=True)
