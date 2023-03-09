from rest_framework import serializers
from .models import Film
from .models import Afish

class Filmsterializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class Afishsterializer(serializers.ModelSerializer):
    class Meta:
        model=Afish
        fields = '__all__'