from rest_framework import serializers
from django.contrib.auth import get_user_model

from .utils import normalize_phone
from .models import Client


User = get_user_model()


class AddManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('full_name', 'email', 'phone_number', 'password')

    def validate_phone(self, phone):
        phone = normalize_phone(phone)
        if len(phone) != 13:
            raise serializers.ValidationError('Invalid phone format')
        if User.objects.filter(phone=phone).exists():
            raise serializers.ValidationError('Phone already exists')
        return phone
    
    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("full_name", "email", "phone_number", "count" )

class ManagerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("full_name", "email", "phone_number")

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client 
        fields = ("full_name", "phone_number", "contract_number")