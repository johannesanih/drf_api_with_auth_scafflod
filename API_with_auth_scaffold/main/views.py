from rest_framework import generics, permissions
from .models import Example
from .serializers import ExampleSerializer

class ExampleListCreateAPI(generics.ListCreateAPIView):
    serializer_class = ExampleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Example.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExampleDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExampleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Example.objects.filter(user=self.request.user)