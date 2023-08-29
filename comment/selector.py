import django_filters
from type16.models import Comment

class BaseCommentFilter(django_filters.FilterSet):
    mbti = django_filters.CharFilter(field_name='mbti__name')
    article = django_filters.NumberFilter(field_name='article__id')

    class Meta:
        model = Comment
        fields = ('mbti', 'article')


def comment_list(*, filters=None):
    filters = filters or {}

    qs = Comment.objects.all()

    return BaseCommentFilter(filters, qs).qs