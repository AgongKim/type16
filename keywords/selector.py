import django_filters
from type16.models import Comment, Keyword
from django.db.models import QuerySet

class BaseCommentFilter(django_filters.FilterSet):
    mbti = django_filters.CharFilter(field_name='mbti__name')
    article = django_filters.NumberFilter(field_name='article__id')

    class Meta:
        model = Comment
        fields = ('mbti', 'article')


class BaseKeywordFilter(django_filters.FilterSet):
    mbti = django_filters.CharFilter(field_name='mbti__name')

    class Meta:
        model = Keyword
        fields = ('mbti',)


def keyword_list(*, filters:dict=None) -> QuerySet:
    filters = filters or {}

    qs = Keyword.objects.all()

    return BaseKeywordFilter(filters, qs).qs