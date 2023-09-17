from rest_framework import serializers
from type16.models import Comment, Mbti, CommentLike, User,Article

class postCommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all() ,default=serializers.CurrentUserDefault())
    mbti = serializers.SlugRelatedField(slug_field='name', queryset=Mbti.objects.all(), required=False)
    article = serializers.PrimaryKeyRelatedField(queryset=Article.objects.all(), required=False)

    class Meta:
        model = Comment
        fields = "__all__"

    def validate(self,data):
        if 'content' not in data:
            raise serializers.ValidationError("content is required")
        if 'article' in data and 'mbti' in data:
            raise serializers.ValidationError("only one of article or mbti is required")
        if 'article' not in data and 'mbti' not in data:
            raise serializers.ValidationError("article or mbti is required")
        return data
    
    
class getCommentSerializer(serializers.ModelSerializer):
    mbti = serializers.SlugRelatedField(slug_field='name', queryset=Mbti.objects.all())
    like_count = serializers.SerializerMethodField(read_only=True)
    is_like = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
    
    def get_like_count(self, obj):
        return obj.commentlike_set.count()
    
    def get_is_like(self, obj):
        if self.context['request'].user.is_authenticated:
            if CommentLike.objects.filter(comment=obj, user=self.context['request'].user).exists():
                return True
        return False


class postCommentLikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all() ,default=serializers.CurrentUserDefault())
    comment = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), required=True)

    class Meta:
        model = CommentLike
        fields = "__all__"