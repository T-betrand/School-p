from dataclasses import field 
from rest_framework import serializers 


from .models import User, ServiceProvider, Skills, Jobs


class UserSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    password  = serializers.CharField(required=False)
    photo = serializers.CharField(required=False)
    location = serializers.CharField(required=False)

    class Meta:
        model = User 
        fields = '__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['name', 'email']




class ServiceProviderSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    photo = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    user_name = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    location = serializers.CharField(required=False)
    skills = serializers.CharField(required=False)
    
    class Meta:
        model = ServiceProvider 
        fields = '__all__'


class SkillsSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    photo = serializers.CharField(required=False)

    class Meta:
        model = Skills 
        fields = '__all__'


class JobsSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(required=False)
    service_providers_id = serializers.CharField(required=False)
   
    class Meta:
        model = Jobs 
        fields = '__all__'


# class PhotoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Photo 
#         fields = '__all__'