from importlib.resources import contents
from pyexpat import model
from unicodedata import category
from django.db import models
from type16.constants import BOARD_CATEGORIES
from type16.models import ModelBase

# Create your models here.
class Article(ModelBase):
    user = models.ForeignKey('user.User', on_delete=models.DO_NOTHING)
    category = models.CharField(max_length=100,choices=BOARD_CATEGORIES)
    title = models.CharField(max_length=1000)
    content = models.TextField()
    hits = models.IntegerField(default=0)
    is_viewable = models.CharField(max_length=10, default='Y')

    class Meta:
        db_table = "t_article"
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Article, self).save(*args, **kwargs)

class ArticleLike(ModelBase):
    article = models.ForeignKey('article.Article', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.DO_NOTHING)

