from drf_yasg import openapi
from utils.swagger_base import *

swagger_keywords_post = PostSwagger(
    params = {
        'mbti_id': openapi.TYPE_INTEGER,
        'content': openapi.TYPE_STRING,
    },
    required = ["content", "mbti_id"],
    summary="[유저토큰 필요] 키워드 작성",
).get_auto_schema()


swagger_keywords_get = GetSwagger(
    params = {
        'mbti': openapi.TYPE_STRING,
        'page': openapi.TYPE_INTEGER,
    },
    examples_={
        "application/json": {
            "gcode": 0,
            "success": True,
            "total_count": 20,
            "count":9999,
            "data" : ["<articledata>"]
        }
    },
    summary="키워드 불러오기 api"
).get_auto_schema()