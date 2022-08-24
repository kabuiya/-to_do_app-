from .models import Activities
from rest_framework import serializers


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = ('id', 'Activity_name', 'date_created')
