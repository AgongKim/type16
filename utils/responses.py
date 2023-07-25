from django.http import JsonResponse
from utils.messages import get_msg


class FailResponse(JsonResponse):
    def __init__(self, msg, **kwargs):
        res = {
            "status" : "500",
            "gcode" : "9000",
            "detail" : msg,
            **kwargs
        }
        super(FailResponse, self).__init__(res,status=500)

class SuccessResponse(JsonResponse):
    def __init__(self, data={}, **kwargs):
        res = {
            "status" : 200,
            "gcode" : "0",
            "data" : data,
            **kwargs
        }
        super(SuccessResponse, self).__init__(res,status=200)
