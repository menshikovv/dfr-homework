from django_filters import rest_framework as filters
from .models import Advertisement

class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = filters.DateFilter(field_name='created_at', lookup_expr='exact')
    status = filters.CharFilter(field_name='status', lookup_expr='exact')

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']
