from rest_framework.routers import DefaultRouter
from .views import BanksViewset

router = DefaultRouter(trailing_slash=False)

router.register('banks', BanksViewset, basename='banks')
