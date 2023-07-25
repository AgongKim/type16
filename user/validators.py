import json
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from type16.models import User, Mbti
from utils.validators import ParamValidator
from utils.responses import FailResponse, get_msg

def user_post_validator(func):
    def wrapper(self, request):
        _data = json.loads(request.body)
        print(_data)
        validator = ParamValidator(_data)
        if validator.required_check(['password', 'username', 'mbti_id' ]):
            return FailResponse(get_msg("parameter_missing"))
        if User.objects.filter(Q(username=_data['username'])).exists():
            return FailResponse(get_msg("duplicate_username"))
        if User.objects.filter(Q(nickname=_data['nickname'])).exists():
            return FailResponse(get_msg("duplicate_nickname"))
        if not Mbti.objects.filter(id=_data.get('mbti_id')).exists():
            return FailResponse(get_msg("mbti_not_found"))
        print("pass")
        return func(self, request)
    return wrapper

def user_patch_validator(func):
    def wrapper(self, request):
        _data = json.loads(request.body)
        if _data.get('username'):
            return FailResponse(get_msg('cant_change_username'))
        if _data.get('password'):
            _data['password'] = make_password(_data['password'])
        return func(self, request, _data)
    return wrapper
