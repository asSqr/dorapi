"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import HealthCheckView

# schema_view = get_schema_view(title='API Lists')

# admin/v1 URL の定義
router = routers.DefaultRouter()
# router.register('muser', views.MUserViewSet, basename='MUser')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('dorapi.urls')),
    path('health_check/', HealthCheckView.as_view({'get': 'get'})),
]

if os.environ.get("ENV") == "local":
    urlpatterns.insert(0, path('', include('app_ex.urls')))
