from django.db import close_old_connections, models
from rest_framework import serializers
from .models import Franquicia


class FranquiciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Franquicia
        fields = ('__all__')

        

