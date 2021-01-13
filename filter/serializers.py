from drf_haystack.serializers import HaystackSerializerMixin
from rest_framework import serializers
from .models import Filter


class FilterListSerializer(serializers.ModelSerializer):
    # offer_delivery_option = serializers.StringRelatedField()
    # status = serializers.StringRelatedField(many=False)
    # total_price = serializers.IntegerField(source='get_total_price')
    # price = serializers.IntegerField()
    is_dhaka = serializers.BooleanField()
    is_khulna = serializers.BooleanField()
    is_male = serializers.BooleanField()
    is_female = serializers.BooleanField()

    class Meta:
        model = Filter
        fields = (
            "id",
            "is_dhaka",
            "is_khulna",
            "is_male",
            "is_female"
        )


class FilterSerializer(HaystackSerializerMixin, FilterListSerializer):
    class Meta(FilterListSerializer.Meta):
        search_fields = (
            "text",
            "id",
            "is_dhaka",
            "is_khulna",
            "is_male",
            "is_female"
        )
        exclude = tuple()