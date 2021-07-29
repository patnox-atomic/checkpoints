##Patnox 27-07-2021

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from checkpoints import views

router = routers.DefaultRouter()
router.register(r'checkpoints', views.CheckedPointsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
