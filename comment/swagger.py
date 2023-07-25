from drf_yasg import openapi
from utils.swagger_base import *

swagger_comment_post = PostSwagger(
    params = {
        "mbti_id": openapi.TYPE_STRING,
        "content": openapi.TYPE_STRING
    },
    required = ["category", "mbti_id"],
    summary = '[유저트큰 필요] 댓글 작성 api'
).get_auto_schema()

swagger_comment_get = GetSwagger(
    params = {
        'offset': openapi.TYPE_INTEGER,
        'limit': openapi.TYPE_INTEGER,
        'article_id': openapi.TYPE_INTEGER
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
        "comment_id": openapi.TYPE_INTEGER,
    }, 
    required = ['comment_id'], 
    summary='[유저토큰 필요] 댓글 좋아요 / 취소 api'
).get_auto_schema()