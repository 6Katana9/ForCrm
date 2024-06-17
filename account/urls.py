from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from . import views

urlpatterns = [
    path('register/', views.AddManagerView.as_view()),
    path('managers/', views.ManagerListAPIView.as_view()),
    path('manager/update/<int:pk>/', views.ManagerUpdateAPIView.as_view()),
    path('manager/delete/<int:pk>/', views.ManagerDeleteAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]