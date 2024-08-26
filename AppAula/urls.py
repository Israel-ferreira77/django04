from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import PessoaViewSet

router = DefaultRouter()
router.register(r"pessoa/",PessoaViewSet )


urlpatterns = [
    path("api/", include(router.urls)),

    
]