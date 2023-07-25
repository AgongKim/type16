import json
from type16.models import Mbti
from type16.constants import BOARD_CATEGORIES
from utils.validators import ParamValidator
from utils.responses import FailResponse, get_msg

def keyword_like_validator(func):
    def wrapper(self,request):
        _data = json.loads(request.body)
        validator = ParamValidator(_data)
        if validator.required_check(['content', 'mbti_id']):
            return FailResponse(get_msg("parameter_missing"))

        if not Mbti.objects.get(pk=_data.get('mbti')).exists():
            return FailResponse(get_msg("mbti_not_found"))
            
        return func(self, request)
    return wrapper