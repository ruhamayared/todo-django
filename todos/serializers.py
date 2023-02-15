from .models import Todo
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Todo
        # The fields that should be included in the serialized output
        fields = ['id', 'subject', 'details']