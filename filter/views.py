from django.shortcuts import render
from drf_haystack.filters import HaystackFilter
from drf_haystack.viewsets import HaystackViewSet
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination

from rest_framework.generics import ListCreateAPIView

from .filter import (
    IsDhakaFilter,
    IsKhulnaFilter,
    IsMaleFilter,
    IsFemaleFilter
)

from .models import Filter
from .serializers import FilterSerializer


# class OfferPagination(PageNumberPagination):
#     page_size = 30
#     max_page_size = 100
#     page_size_query_param = 'page_size'

class FilterList(ListCreateAPIView):

    queryset = Filter.objects.all()
    serializer_class = FilterSerializer

    print("List: ", queryset)
    #     return queryset


class FilterFeedViewSet(HaystackViewSet):
    index_models = [Filter]
    authentication_classes = []
    permission_classes = []
    required_scopes = []
    # pagination_class = OfferPagination

    # queryset = Filter.objects.all()
    serializer_class = FilterSerializer

    # print("ViewSet: ", queryset)

    filter_backends = [
        IsMaleFilter
    ]

    ordering_fields = (
        "id",
        "is_dhaka",
        "is_khulna",
        "is_male",
        "is_female",
        "pub_date"
    )
    ordering = ('pub_date',)

    def get_serializer_context(self):
        context = super(FilterFeedViewSet, self).get_serializer_context()
        return context

