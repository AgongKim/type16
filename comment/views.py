import json
from django.core.paginator import Paginator
from rest_framework.views import APIView

from utils.responses import FailResponse, SuccessResponse, get_msg
from utils.decorators import auth_required

from type16.models import Comment, CommentLike
from .serializers import *
from .swagger import *
from .validators import *


class CommentAPI(APIView):
    swagger_tags = ['comment']

    @swagger_comment_post
    @auth_required
    @comment_post_validator
    def post(self, request):
        try:
            _data = json.loads(request.body)
            _data["user"] = request.user
            article = Comment.objects.create(**_data)
            return SuccessResponse(data = CommentSerializer(article).data)
        except Exception as e:
            print(e)
            return FailResponse(get_msg("internal_error"))
    
    @swagger_comment_get
    def get(self, request):
        offset = request.GET.get('offset', 1)
        limit = request.GET.get('limit', 20)
        article_id = request.GET.get('article_id')

        total_list = Comment.objects.filter(article_id=article_id).order_by('-created_at')

        paginator = Paginator(total_list, limit)
        cutoff_list = paginator.get_page(offset)
        total_count = total_list.count()
        count = len(cutoff_list)
        
        return SuccessResponse(
            total_count=total_count, count=count,
            data=CommentSerializer(cutoff_list, many=True).data)

class CommentLikeAPI(APIView):
    swagger_tags = ['comment']

    @swagger_comment_like
    @auth_required
    @comment_like_validator
    def post(self, request):
        try:
            user = request.user
            _data = json.loads(request.body)
            comment_id = _data.get('comment_id')

            if CommentLike.objects.filter(comment_id=comment_id, user=user).exists():
                CommentLike.objects.filter(comment_id=comment_id, user=user).delete()
            else:
                CommentLike.objects.create(
                    user = user,
                    comment_id = comment_id
                )
        except Exception as e:
            print(e)
            return FailResponse(get_msg("invalid_format"))
