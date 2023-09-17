import django_filters
from django.db.models import QuerySet
from rest_framework.request import Request
from type16.models import Comment,CommentLike

class BaseCommentFilter(django_filters.FilterSet):
    mbti = django_filters.CharFilter(field_name='mbti__name')
    article = django_filters.NumberFilter(field_name='article__id')

    class Meta:
        model = Comment
        fields = ('mbti', 'article')


def comment_list(*, filters:dict=None) -> QuerySet:
    filters = filters or {}

    qs = Comment.objects.all()

    return BaseCommentFilter(filters, qs).qs.order_by('-id')

def try_delete_commentlike(*, request:Request) -> bool:
    user = request.user
    comment_id = request.data.get('comment')
    if CommentLike.objects.filter(comment_id=comment_id, user=user).exists():
        CommentLike.objects.filter(comment_id=comment_id, user=user).delete()
        return True
    return False