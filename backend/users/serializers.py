from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    input = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'score', 'input']

    def update_score(self, instance, validated_data):
        input_value = validated_data.pop('input', 0)
        instance.score += input_value
        instance.save()
        return instance
