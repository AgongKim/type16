from rest_framework import serializers
from type16.models import Article, Comment, User, Mbti
from type16.constants import BOARD_CATEGORIES

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

class postArticleSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all() ,default=serializers.CurrentUserDefault())
    category = serializers.ChoiceField(choices=BOARD_CATEGORIES)
    hits = serializers.IntegerField(default=0, required=False)
    is_viewable = serializers.CharField(max_length=10, default='Y', required=False)

    class Meta:
        model = Article
        fields = "__all__"

    
class getArticleSerializer(serializers.ModelSerializer):
    category = serializers.ChoiceField(choices=BOARD_CATEGORIES)

    class Meta:
        model = Article
        fields = "__all__"
    