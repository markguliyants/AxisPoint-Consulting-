from .models import GreetingsData
from rest_framework import serializers


class GreetingsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GreetingsData
        fields =['id', 'category', 'from_field', 'title', 'text', 'date', 'id_column']
