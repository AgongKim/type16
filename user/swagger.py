from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from utils.swagger_base import GetSwagger, PostSwagger

swagger_user_post = PostSwagger(
    params = {
        "username": openapi.TYPE_STRING,
        "password": openapi.TYPE_STRING,
        "nickname": openapi.TYPE_STRING,
        "mbti_id": openapi.TYPE_INTEGER
    },
    required = ["username", "password", "nickname", "mbti_id"],
    summary = '유저 생성 api'
).get_auto_schema()

swagger_user_patch = PostSwagger(
    params = {
        "password": openapi.TYPE_STRING,
        "nickname": openapi.TYPE_STRING,
        "mbti_id": openapi.TYPE_INTEGER
    },
    required = [],
    summary = '유저 수정 api'
).get_auto_schema()

swagger_user_delete = GetSwagger(
    params = {},
    examples_={
        "application/json": {
            "gcode": 0,
            "success": True,
        }
    },
    summary="유저 삭제 api"
).get_auto_schema()

swagger_user_detail = GetSwagger(
    params = {
        "user_id": openapi.TYPE_INTEGER
    },
    examples_={
        "application/json": {
            "gcode": 0,
            "success": True,
            "data": "<userdata>"
        }
    },
    summary="유저 상세보기 api"
).get_auto_schema()
