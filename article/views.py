import json
from django.core.paginator import Paginator
from rest_framework.views import APIView

from utils.responses import FailResponse, SuccessResponse, get_msg
from utils.decorators import auth_required

from type16.models import Article, Comment, ArticleLike
from comment.serializers import CommentSerializer

from .swagger import *
from .validators import *
from .serializers import *

class ArticleAPI(APIView):
    swagger_tags = ['article']

    @swagger_article_post
    @auth_required
    @article_post_validator
    def post(self, request):
        try:
            _data = json.loads(request.body)
            _data["user"] = request.user
            article = Article.objects.create(**_data)
            return SuccessResponse(data = ArticleSerializer(article).data)
        except Exception as e:
            print(e)
            return FailResponse(get_msg("internal_error"))
    
    @swagger_article_get
    def get(self, request):
        offset = request.GET.get('offset', 1)
        limit = request.GET.get('limit', 20)
        category = request.GET.get('category')

        total_list = Article.objects.all()
        if category:
            total_list.filter(category=category)
        total_list.order_by('-created_at')

        paginator = Paginator(total_list, limit)
        cutoff_list = paginator.get_page(offset)
        total_count = total_list.count()
        count = len(cutoff_list)
        
        return SuccessResponse(
            total_count=total_count, count=count,
            data=ArticleSerializer(cutoff_list, many=True).data)


class ArticleDetailAPI(APIView):
    swagger_tags = ['article']

    @swagger_article_detail
    def get(self, request, article_id):
        try:
            article = Article.objects.get(id=article_id)
            comment = Comment.objects.filter(article_id=article_id)

            return SuccessResponse(
                data=ArticleSerializer(article, many=False).data,
                comment=CommentSerializer(comment, many=True).data
            )
        except Exception as e:
            print(e)
            return FailResponse(get_msg("invalid_format")) 


class ArticleCategoriesAPI(APIView):
    swagger_tags = ['category']
    
    @swagger_article_categories
    def get(self,request):
        from type16.constants import BOARD_CATEGORIES

        result = {}
        for key,value in BOARD_CATEGORIES:
            result[key] = value

        return SuccessResponse(data=result)
    

class ArticleLikeAPI(APIView):
    swagger_tags = ['article']

    @swagger_article_like
    @auth_required
    @article_like_validator
    def post(self, request):
        try:
            user = request.user
            _data = json.loads(request.body)
            article_id = _data.get('article_id')

            if ArticleLike.objects.filter(article_id=article_id, user=user).exists():
                ArticleLike.objects.filter(article_id=article_id, user=user).delete()
            else:
                ArticleLike.objects.create(
                    user = user,
                    article_id = article_id
                )
        except Exception as e:
            print(e)
            return FailResponse(get_msg("invalid_format"))
