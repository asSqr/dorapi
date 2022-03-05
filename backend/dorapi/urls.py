from django.urls import path, include
# import os
from . import views
from rest_framework import routers
# from rest_framework_nested import routers as routers_nested


router = routers.SimpleRouter()

router.register(r'mgadgets', views.MGadgetView, basename='mgadgets')

# if os.environ.get("ENV") == "local": router.register(r'tests', views.TestView, basename='tests')


# URL 定義
urlpatterns = [
    path('me/', views.MeView.as_view({'get': 'get'})),
    path('', include(router.urls)),
]      # noqa
