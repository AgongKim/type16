import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .swagger import *
from .serializers import *
from .selector import *
from type16.models import Keyword, Mbti
from utils.responses import FailResponse, SuccessResponse, get_msg
from utils.decorators import auth_required
from django.db.models import Q, Count
from django.contrib.auth.models import AnonymousUser
from utils.drfcustoms import get_paginated_response

class KeywordCreateAPI(APIView):
    swagger_tags = ['keywords']
    
    @swagger_keywords_post
    # @auth_required
    def post(self, request):
        serializer = postKeywordSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

    class FilterSerializer(serializers.Serializer):
        mbti = serializers.CharField(required=True)

    @swagger_keywords_get
    def get(self, request):
        page_size = 20

        param_serializer = self.FilterSerializer(data=request.query_params)
        param_serializer.is_valid(raise_exception=True)

        page = int(request.query_params.get('page',1))
        offset = ( page - 1 ) * page_size
        limit = page_size * page

        queryset = keyword_list(filters=param_serializer.validated_data)
        
        data = queryset.values('content').annotate(count=Count('content')).order_by('-count')[offset:limit]
        
        return Response(data=dict(keywords=data), status=status.HTTP_201_CREATED)
