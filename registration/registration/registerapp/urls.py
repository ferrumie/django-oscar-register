from django.urls import path
from .views import RegisterAPIView, RegisterListAPIView


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('list/', RegisterListAPIView.as_view(), name='register-list'),
]