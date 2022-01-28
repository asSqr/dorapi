from django.urls import path, include
import os
from .views import MeView
from rest_framework import routers
from rest_framework_nested import routers as routers_nested


router = routers.SimpleRouter()

# if os.environ.get("ENV") == "local":
    # router.register(r'tests', views.TestView, basename='tests')


# URL 定義
urlpatterns = [
    path('me/', MeView.as_view({'get': 'get'})),
    path('', include(router.urls)),
]
