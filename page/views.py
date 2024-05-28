from rest_framework import status, generics, filters, mixins, viewsets
from page.models import *
from page.filters import LogatFilter
from page.pagination import LargeResultsSetPagination
from django_filters.rest_framework import DjangoFilterBackend
from page.serializers import LogatSerializer


class GetLugatViewSet(generics.ListAPIView, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = LogatSerializer
    permission_classes = []
    queryset = Logat.objects.order_by('-id').all()
    filterset_class = LogatFilter
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

