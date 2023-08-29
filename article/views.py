import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from utils.drfcustoms import get_paginated_response

from utils.responses import FailResponse, SuccessResponse, get_msg
from utils.decorators import auth_required

from type16.models import Article, Comment, ArticleLike

from .swagger import *
from .serializers import *
from .selector import *

class ArticleAPI(APIView):
    swagger_tags = ['article']

    @swagger_article_post
    @auth_required
    def post(self, request):
        serializer = postArticleSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    class FilterSerializer(serializers.Serializer):
        category = serializers.CharField(required=True)
        page = serializers.IntegerField(required=False)
        
    class Pagination(PageNumberPagination):
        page_size = 20

    @swagger_article_get
    def get(self, request):
        param_serializer = self.FilterSerializer(data=request.query_params)
        param_serializer.is_valid(raise_exception=True)

        comments = article_list(filters=param_serializer.validated_data)

        return get_paginated_response(
                pagination_class=self.Pagination,
                serializer_class=getArticleSerializer,
                queryset=comments,
                request=request,
                view=self
            )


class ArticleDetailAPI(APIView):
    swagger_tags = ['article']

    @swagger_article_detail
    def get(self, request, article_id):
        article = article_get(id=article_id)

        serializer = getArticleSerializer(article)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ArticleCategoriesAPI(APIView):
    swagger_tags = ['category']
    
    @swagger_article_categories
    def get(self,request):
        from type16.constants import BOARD_CATEGORIES

        result = {}
        for key,value in BOARD_CATEGORIES:
            result[key] = value

        return Response(data=result, status=status.HTTP_200_OK)
    

class ArticleLikeAPI(APIView):
    swagger_tags = ['article']

    @swagger_article_like
    @auth_required
    def post(self, request):
        user = request.user
        _data = request.data
        article_id = _data.get('article')

        if ArticleLike.objects.filter(article_id=article_id, user=user).exists():
            ArticleLike.objects.filter(article_id=article_id, user=user).delete()
            status = "unliked"
        else:
            ArticleLike.objects.create(
                user = user,
                article_id = article_id
            )
            status = "liked"

        return Response(data={"status":status}, status=status.HTTP_200_OK)
