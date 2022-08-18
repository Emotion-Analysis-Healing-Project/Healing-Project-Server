from rest_framework import serializers
from .models import User, Asmr, Video

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']

class AsmrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asmr
        fields = ['emotion', 'file']
    
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['emotion', 'url']