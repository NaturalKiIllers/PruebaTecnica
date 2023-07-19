from rest_framework import serializers
from .models import User, Context, Event

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = '__all__'
    
class ContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Context
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event 
        fields = '__all__'
        