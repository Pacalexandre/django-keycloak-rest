from django.urls import Resolver404
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from .serializers import BanksSerializers
from .models import Banks


def exception_view(*args, **kwargs):

    value = kwargs['exception']
    print(value.__class__)

    return None


class BanksViewset(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = BanksSerializers
    queryset = Banks.objects.all()
