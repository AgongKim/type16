from drf_yasg import openapi
from utils.swagger_base import *

swagger_article_post = PostSwagger(
    params = {
        "category": openapi.TYPE_STRING,
        "title": openapi.TYPE_STRING,
        "content": openapi.TYPE_STRING
    },
    required = ["category", "title", "content"],
    summary = '[유저트큰 필요] 게시글 작성 api'
).get_auto_schema()

swagger_article_get = GetSwagger(
    params = {
        'page' : openapi.TYPE_INTEGER,
        'category' : openapi.TYPE_STRING,
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
    summary="게시글 불러오기 api"
).get_auto_schema()

swagger_article_detail = GetSwagger(
    params={}, 
    examples_={
        "application/json": {
            "gcode": 0,
            "success": True,
            "data" : "<articledata>",
            "comment" : ["<commentdata>"]
        }
    }, 
    summary="게시물 상세보기 api"
).get_auto_schema()

swagger_article_categories = GetSwagger(
    params={},
    examples_={
        "application/json": {
            "gcode": 0,
            "success": True,
            "data" : ["category"],
        }
    }, summary="카테고리 목록 api"
).get_auto_schema()

swagger_article_like = PostSwagger(
    params={
        "article": openapi.TYPE_INTEGER,
    }, 
    required = ['article'], 
    summary='[유저토큰 필요] 게시글 좋아요 / 취소 api'
).get_auto_schema()