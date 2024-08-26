from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path
from .viewsets import serializers
from .serializers import views

router = DefaultRouter()
router.register(prefix="f1", viewset= serializers )


urlpatterns = [
    path("api/", include(router.urls)),
    path('mostrar/', views.mostrar),
    path('form/', views.formulario, name='form')
    
]