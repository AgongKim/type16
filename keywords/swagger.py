from drf_yasg import openapi
from utils.swagger_base import *

swagger_keywords_create = PostSwagger(
    params = {
        'mbti_id': openapi.TYPE_INTEGER,
        'content': openapi.TYPE_STRING,
    },
    required = ["content", "mbti_id"],
    summary="[유저토큰 필요] 키워드 작성",
).get_auto_schema()

