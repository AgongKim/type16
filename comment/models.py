from django.db import models
from type16.models import ModelBase

# Create your models here.
class Comment(ModelBase):
    article = models.ForeignKey('article.Article', on_delete=models.DO_NOTHING, null=True, blank=False)
    mbti = models.ForeignKey('type16.Mbti', on_delete=models.DO_NOTHING, null=True, blank=False)
    user = models.ForeignKey('user.User', on_delete=models.DO_NOTHING)
    content = models.TextField()
    
    class Meta:
        db_table = "t_comment"

class CommentLike(ModelBase):
    comment = models.ForeignKey(to=Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(to='user.User', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "t_comment_like"
        unique_together = ('comment', 'user',)