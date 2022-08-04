from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin
from .serializers import BanksSerializers
from .models import Banks


class BanksViewset(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = BanksSerializers
    queryset = Banks.objects.all
