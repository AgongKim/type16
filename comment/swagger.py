from drf_yasg import openapi
from utils.swagger_base import *

swagger_comment_post = PostSwagger(
    params = {
        'article': openapi.TYPE_INTEGER,
        'mbti': openapi.TYPE_STRING,
        "content": openapi.TYPE_STRING
    },
    required=[],
    summary = '[유저트큰 필요] 댓글 작성 api'
).get_auto_schema()

swagger_comment_get = GetSwagger(
    params = {
        'page': openapi.TYPE_INTEGER,
        'article': openapi.TYPE_INTEGER,
        'mbti': openapi.TYPE_STRING
    },
    examples_={
        "application/json": {
            "gcode": 0,
            "success": True,
            "total_count": 20,
            "count":9999,
            "data" : ["<commentdata>"]
        }
    },
    summary="댓글 불러오기 api"
).get_auto_schema()

swagger_comment_like = PostSwagger(
    params={
        "comment": openapi.TYPE_INTEGER,
    }, 
    required = ['comment_id'], 
    examples_={
        "application/json": {
            "status": "liked|unliked"
        }
    },
    summary='[유저토큰 필요] 댓글 좋아요 / 취소 api'
).get_auto_schema()