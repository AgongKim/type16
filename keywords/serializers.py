from rest_framework import serializers
from type16.models import Keyword, Mbti, User

class postKeywordSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all() ,default=serializers.CurrentUserDefault())
    mbti = serializers.SlugRelatedField(slug_field='name', queryset=Mbti.objects.all())

    class Meta:
        model = Keyword
        fields = "__all__"
