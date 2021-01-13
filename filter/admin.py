from django.contrib import admin
from .models import Filter


class FilterAdmin(admin.ModelAdmin):
    list_display = ['ifa', 'is_dhaka', 'is_khulna', 'is_male', 'is_female', 'pub_date']
    list_filter = ['is_male', 'is_female']


admin.site.register(Filter, FilterAdmin)
