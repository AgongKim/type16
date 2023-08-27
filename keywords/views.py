import json
from rest_framework.views import APIView
from .swagger import *
from .serializers import KeywordSerializer
from type16.models import Keyword, Mbti
from utils.responses import FailResponse, SuccessResponse, get_msg
from utils.decorators import auth_required
from django.db.models import Q, Count
from django.contrib.auth.models import AnonymousUser

class KeywordCreateAPI(APIView):
    swagger_tags = ['keywords']
    
    @swagger_keywords_post
    # @auth_required
    def post(self, request):
        try:
            _data = json.loads(request.body)
            user = request.user if not isinstance(request.user, AnonymousUser) else None
            q = {}
            if _data.get('mbti_id'):
                q['id'] =  _data.get('mbti_id')
            if _data.get('mbti'):
                q['name'] = _data.get('mbti')
            if not q or not _data.get('content'):
                raise FailResponse('parameter_missing')

            mbti = Mbti.objects.get(**q)
            # 데이터 수집을 위해 로그인 x 여러개 o
            # old_one = Keyword.objects.filter(user=user, mbti=_data.get('mbti_id')).first()
            # if old_one:
            #     old_one.content = _data.get('content')
            #     old_one.save(update_fields=['content'])
            # else:
            Keyword.objects.create(
                user = user,
                mbti = mbti,
                content = _data.get('content'),
            )
            return SuccessResponse()

        except Exception as e:
            print(e)
            return FailResponse(get_msg("invalid_format"))
    
    @swagger_keywords_get
    def get(self, request):
        try:
            _mbti = request.GET.get('mbti')
            mbti_id = request.GET.get('mbti_id')
            mbti = Mbti.objects.get( Q(id=mbti_id)| Q(name=_mbti))
            keywords = Keyword.objects.filter(mbti=mbti)\
                .values('content')\
                .annotate(count=Count('content'))\
                .order_by('-count')[0:30]

            return SuccessResponse(
                data=list(keywords),
            )
        except (Mbti.DoesNotExist, Mbti.MultipleObjectsReturned):
            return FailResponse(get_msg('mbti_not_found'))
        except Exception as e:
            print(e)
            return FailResponse(get_msg("invalid_format"))
