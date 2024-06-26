"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/items', views.v1_items),
    path('api/v1/item/<int:item_id>', views.v1_item_by_id),
    path('api/v1/items/search/<str:keyword>', views.v1_item_search),
    path('api/v1/location/<int:location_id>', views.v1_location_by_id),
    path('api/v1/location/<int:location_id>/photo', views.v1_location_photo),
    path('api/v1/properties', views.v1_properties)
]
