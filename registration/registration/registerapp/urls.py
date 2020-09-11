from django.urls import path
from .views import RegisterCreateView, RegisterListView


urlpatterns = [
    path('register/', RegisterCreateView.as_view(), name='register'),
    path('list/', RegisterListView.as_view(), name='register-list'),
]