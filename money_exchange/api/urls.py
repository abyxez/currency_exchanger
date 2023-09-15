from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RateViewSet

app_name = "api"

router = DefaultRouter()

router.register("rates", RateViewSet, "rates")

urlpatterns = [
    path("", include(router.urls)),
]
