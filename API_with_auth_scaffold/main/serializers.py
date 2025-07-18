from rest_framework import serializers
from .models import Example

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ('id', 'title', 'description', 'completed', 'created_at')
