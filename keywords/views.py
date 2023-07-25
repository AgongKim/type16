import json
from rest_framework.views import APIView
from .swagger import *
from type16.models import Keyword, Mbti
from utils.responses import FailResponse, SuccessResponse, get_msg
from utils.decorators import auth_required
from django.db.models import Q

class KeywordCreateAPI(APIView):
    swagger_tags = ['keywords']
    
    @swagger_keywords_create
    @auth_required
    def post(self, request):
        try:
            _data = json.loads(request.body)
            user = request.user
            
            old_one = Keyword.objects.filter(user=user, mbti=_data.get('mbti_id')).first()
            if old_one:
                old_one.content = _data.get('content')
                old_one.save(update_fields=['content'])
            else:
                Keyword.objects.create(
                    user = request.user,
                    mbti_id = _data.get('mbti_id'),
                    content = _data.get('content'),
                )
            return SuccessResponse()

        except Exception as e:
            print(e)
            return FailResponse(get_msg("invalid_format"))
