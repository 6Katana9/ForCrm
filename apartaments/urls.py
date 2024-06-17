from django.urls import path

from . import views

urlpatterns = [
    path('', views.ApartamentListCreateAPIView.as_view()),
    path('update/<int:pk>/', views.ApartamentUpdateAPIView.as_view()),
    path('delete/<int:pk>/', views.ApartamentDeleteAPIView.as_view()),
]