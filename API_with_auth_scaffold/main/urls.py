from django.urls import path
from .views import ExampleListCreateAPI, ExampleDetailAPI

urlpatterns = [
    path('example/', ExampleListCreateAPI.as_view(), name='example-list-create'),
    path('example/<int:pk>/', ExampleDetailAPI.as_view(), name='example-detail'),
]