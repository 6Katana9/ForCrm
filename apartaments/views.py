from copy import deepcopy

from rest_framework.generics import UpdateAPIView, ListCreateAPIView, DestroyAPIView
from rest_framework.response import Response

from account.models import Client

from .models import Apartament
from .serializers import ApartamentSerializer, ApartamentUpdateSerializer


    
class ApartamentListCreateAPIView(ListCreateAPIView):
    queryset = Apartament.objects.all()
    serializer_class = ApartamentSerializer


class ApartamentUpdateAPIView(UpdateAPIView):
    queryset = Apartament.objects.all()
    serializer_class = ApartamentUpdateSerializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = deepcopy(request.data)
        client = data.pop("client")
        status = data.pop('status')
        client = Client.objects.create(**client)
        instance.client = client
        instance.status = status
        instance.save()
        serializer = self.get_serializer(instance)

        return Response(serializer.data)


class ApartamentDeleteAPIView(DestroyAPIView):
    queryset = Apartament.objects.all()
    serializer_class = ApartamentSerializer
    