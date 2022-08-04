"""Serializers"""
from rest_framework.serializers import ModelSerializer
from .models import Banks

class BanksSerializers(ModelSerializer):

    class Meta:
        model = Banks
        fields = ['ispb','name','code','fullName']
