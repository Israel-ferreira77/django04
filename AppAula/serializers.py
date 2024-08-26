from rest_framework.serializers import ModelSerializer
from .models import teste


class (ModelSerializer):
    class Meta:
        models = ModelSerializer
        fields = ['nome' 'sobrenome']