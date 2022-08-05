""" Viewsset DjangoRestFramework """
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from .serializers import BanksSerializers
from .models import Banks


class BanksViewset(ListModelMixin,RetrieveModelMixin,
                CreateModelMixin,UpdateModelMixin,GenericViewSet):
    """Listagem de Bancos - ApiBrasil"""
    serializer_class = BanksSerializers
    queryset = Banks.objects.all()
