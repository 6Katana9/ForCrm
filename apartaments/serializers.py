from rest_framework import serializers

from account.models import Client

from .models import Apartament

class ApartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartament
        fields = ("apartment_number", "object_name", "floor", "square", "date", "status", "price", "client")


class ApartamentUpdateSerializer(serializers.ModelSerializer):
    client = Client()

    class Meta:
        model = Apartament
        fields = ("client", "status")


