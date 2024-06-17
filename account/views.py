from copy import deepcopy

from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema



from .models import Client
from .serializers import AddManagerSerializer, ManagerSerializer, ManagerUpdateSerializer


User = get_user_model()


class AddManagerView(APIView):
    @swagger_auto_schema(request_body=AddManagerSerializer())
    def post(self, request):
        data = request.data
        serializer = AddManagerSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response('Регистрация прошла успешно!', status=201)
    
class ManagerListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = ManagerSerializer

class ManagerUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ManagerUpdateSerializer

class ManagerDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ManagerSerializer
    

    