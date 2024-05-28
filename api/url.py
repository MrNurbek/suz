from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from page.views import *


router = routers.DefaultRouter()

router.register(r'get', GetLugatViewSet),


urlpatterns = [

]
urlpatterns += router.urls
