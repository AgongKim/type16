from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response

from utils.responses import FailResponse, get_msg
from utils.decorators import auth_required
from utils.drfcustoms import get_paginated_response

from type16.models import Comment, CommentLike
from .serializers import *
from .swagger import *
from .selector import *


class CommentAPI(APIView):
    swagger_tags = ['comment']
    queryset = Comment.objects.all()

    @swagger_comment_post
    @auth_required
    def post(self, request, *args, **kwargs):
        serializer = postCommentSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
    class FilterSerializer(serializers.Serializer):
        mbti = serializers.CharField(required=False)
        article = serializers.IntegerField(required=False)
        page = serializers.IntegerField(required=False)

        def validate(self, data):
            if 'article' in data and 'mbti' in data:
                raise serializers.ValidationError("only one of article or mbti is required")
            if 'article' not in data and 'mbti' not in data:
                raise serializers.ValidationError("article or mbti is required")
            return data
    
    class Pagination(PageNumberPagination):
        page_size = 20
    
    @swagger_comment_get
    def get(self, request, *args, **kwargs):
        param_serializer = self.FilterSerializer(data=request.query_params)
        param_serializer.is_valid(raise_exception=True)

        comments = comment_list(filters=param_serializer.validated_data)

        return get_paginated_response(
                pagination_class=self.Pagination,
                serializer_class=getCommentSerializer,
                queryset=comments,
                request=request,
                view=self
            )
        

class CommentLikeAPI(APIView):
    swagger_tags = ['comment']

    @swagger_comment_like
    @auth_required
    def post(self, request):
        user = request.user
        _data = request.data
        comment_id = _data.get('comment')

        if CommentLike.objects.filter(comment_id=comment_id, user=user).exists():
            CommentLike.objects.filter(comment_id=comment_id, user=user).delete()
            status = "unliked"
        else:
            CommentLike.objects.create(
                user = user,
                comment_id = comment_id
            )
            status = "liked"

        return Response(data={"status":status}, status=status.HTTP_200_OK)