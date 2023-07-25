
from django.db import models
from type16 import constants

class ModelBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

# Create your models here.
class Mbti(ModelBase):
    EI_CHOICES = [
        ('E', 'Extroversion'),
        ('I', 'Introversion')
    ]
    NS_CHOICES = [
        ('N', 'iNtuition'),
        ('S', 'Sensing')
    ]
    TF_CHOICES = [
        ('T', 'Thinking'),
        ('F', 'Feeling')
    ]
    PJ_CHOICES = [
        ('P', 'Perceiving'),
        ('J', 'Judging')
    ]

    name=models.CharField(max_length=10, choices=constants.MBTI_TYPE)
    title=models.CharField(max_length=200, help_text="타이틀(ex:전략가,성인군자..)")
    description=models.TextField(help_text="해당 mbti에 대한 설명")
    image_url=models.CharField(max_length=3000)
    ei=models.CharField(max_length=1, choices=EI_CHOICES, help_text="주의초점")
    ns=models.CharField(max_length=1, choices=NS_CHOICES, help_text="인식기능")
    tf=models.CharField(max_length=1, choices=TF_CHOICES, help_text="판단기능")
    pj=models.CharField(max_length=1, choices=PJ_CHOICES, help_text="생활양식")
    class Meta:
        db_table = "t_mbti"
    
    def __str__(self):
        return self.name

from user.models import * 
from article.models import *
from comment.models import *
from keywords.models import *
