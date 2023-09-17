import django_filters
from django.db.models import Model, QuerySet
from rest_framework.request import Request
from type16.models import Article, ArticleLike, User
from type16.constants import BOARD_CATEGORIES

class BaseArticleFilter(django_filters.FilterSet):
    category = django_filters.ChoiceFilter(choices=BOARD_CATEGORIES)

    class Meta:
        model = Article
        fields = ('category',)


def article_list(*, filters:dict=None) -> QuerySet:
    filters = filters or {}

    qs = Article.objects.all()

    return BaseArticleFilter(filters, qs).qs.order_by('-id')


def article_get(*, id:int) -> Model:
    return Article.objects.get(id=id)


def try_delete_articlelike(*, request:Request) -> bool:
    user = request.user
    article_id = request.data.get('article')
    if ArticleLike.objects.filter(article_id=article_id, user=user).exists():
        ArticleLike.objects.filter(article_id=article_id, user=user).delete()
        return True
    return False