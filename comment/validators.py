import json
from type16.models import Comment
from utils.validators import ParamValidator
from utils.responses import FailResponse, get_msg

def comment_post_validator(func):
    def wrapper(self, request):
        _data = json.loads(request.body)
        validator = ParamValidator(_data)
        if validator.required_check(['content']):
            return FailResponse(get_msg("parameter_missing"))
        
        if not ('article_id' in _data or 'mbti_id' in _data):
            return FailResponse(get_msg("parameter_missing"))

        return func(self, request)
    return wrapper

def comment_like_validator(func):
    def wrapper(self,request):
        _data = json.loads(request.body)
        validator = ParamValidator(_data)
        if validator.required_check(['comment_id']):
            return FailResponse(get_msg("parameter_missing"))
        
        if not Comment.objects.filter(id=_data.get('comment_id')).exists():
            return FailResponse(get_msg('comment_not_found'))

        return func(self, request)
    return wrapper