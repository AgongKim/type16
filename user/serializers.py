from rest_framework import serializers
from type16.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class postUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=100, required=True)
    hits = serializers.IntegerField(default=0, required=False)
    is_viewable = serializers.CharField(max_length=10, default='Y', required=False)

    class Meta:
        model = User
        fields = "__all__"