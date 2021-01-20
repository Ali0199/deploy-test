from rest_framework import serializers
from .models import kraska

class KraskaSerializer(serializers.ModelSerializer):
    class Meta:
        model=kraska
        fields=['id', 'name', 'karobka', 'soni', 'narxi', 'date']
    
