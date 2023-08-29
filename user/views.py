import json
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from type16.models import User, Mbti
from utils.responses import FailResponse, SuccessResponse, get_msg
from utils.decorators import auth_required

from .swagger import *
from .serializers import *

class UserAPI(APIView):
    swagger_tags = ['users']


    @swagger_user_post
    def post(self, request):
        try:
            ## 추후 인증 과정 및 카카오 로그인 등 구현
            with transaction.atomic():
                _data = json.loads(request.body)
                _data['password'] = make_password(_data['password'])
                u = User.objects.create(**_data)
            return SuccessResponse(UserSerializer(u).data)

        except Exception as e:
            print(e)
            return FailResponse(get_msg("invalid_format"))
    
    @swagger_user_patch
    @auth_required
    def patch(self, request, _data):
        u = request.user
        if 'password' in _data:
            u.password = _data['password']
        if 'nickname' in _data:
            u.nickname = _data['nickname']
        if 'mbti_id' in _data:
            mbti = Mbti.objects.get(id=_data.get('mbti_id'))
            u.mbti = mbti
        u.save()
        refresh = RefreshToken.for_user(u)
        data = dict(
            user = UserSerializer(u).data,
            refresh = str(refresh),
            access = str(refresh.access_token),
        )
        return SuccessResponse(data)
    
    @swagger_user_delete
    @auth_required
    def delete(self, request):
        user = request.user
        user.status = User.STATUS_ABNORMAL
        user.is_active = False
        user.save()
        return SuccessResponse()
    
    @swagger_user_get
    @auth_required
    def get(self, request):
        return SuccessResponse(UserSerializer(request.user).data)


class UserDetailAPI(APIView):
    swagger_tags = ['users']

    @auth_required
    @swagger_user_detail
    def get(self, request):
        _data = json.loads(request.body)
        user = None
        if 'user_id' in _data:
            user = User.objects.filter(id=_data.get('user_id'))
        if not user:
            user = request.user
        return SuccessResponse(UserSerializer(user).data)

