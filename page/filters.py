import django_filters
from page.models import *


class LogatFilter(django_filters.FilterSet):
    user = django_filters.ModelChoiceFilter(queryset=Logat.objects.all())

    class Meta:
        model = Logat
        fields = ['name']


