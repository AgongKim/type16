from django.db import models
from type16.models import ModelBase

# Create your models here.
class Keyword(ModelBase):
    mbti = models.ForeignKey('type16.Mbti', on_delete=models.DO_NOTHING)
    user = models.ForeignKey('user.User', null=True, on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=10)

    class Meta:
        db_table = "t_keyword"