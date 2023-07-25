import json
from type16.models import Article
from type16.constants import BOARD_CATEGORIES
from utils.validators import ParamValidator
from utils.responses import FailResponse, get_msg

def article_post_validator(func):
    def wrapper(self, request):
        _data = json.loads(request.body)
        validator = ParamValidator(_data)
        if validator.required_check(['category', 'title','content']):
            return FailResponse(get_msg("parameter_missing"))
        
        if validator.type_check([
            ('category', BOARD_CATEGORIES)
        ]):
            return FailResponse(get_msg('invalid_format'))
        
        if _data.get('hits'):
            return FailResponse(get_msg("no_hits_control"))

        return func(self, request)
    return wrapper

def article_like_validator(func):
    def wrapper(self,request):
        _data = json.loads(request.body)
        validator = ParamValidator(_data)
        if validator.required_check(['article_id']):
            return FailResponse(get_msg("parameter_missing"))
        
        if not Article.objects.filter(id=_data.get('article_id')).exists():
            return FailResponse(get_msg('article_not_found'))

        return func(self, request)
    return wrapper