import django_filters
from .models import visitHistory

class visitHistoryFilter(django_filters.FilterSet):
    class Meta:
        model = visitHistory
        fields = ['visit_date', 'villageName', 'visit_name', ]