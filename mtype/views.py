from django.http import HttpResponse
from django.template import loader

from type16.models import Mbti

def detail(request, mbti):
    mbti = Mbti.objects.get(name=mbti)
    template = loader.get_template("mtype/detail.html")
    context = {
        "mbti": mbti,
    }
    return HttpResponse(template.render(context, request))