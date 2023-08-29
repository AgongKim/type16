import django_filters
from type16.models import Article
from type16.constants import BOARD_CATEGORIES

class BaseArticleFilter(django_filters.FilterSet):
    category = django_filters.ChoiceFilter(choices=BOARD_CATEGORIES)

    class Meta:
        model = Article
        fields = ('category',)


def article_list(*, filters=None):
    filters = filters or {}

    qs = Article.objects.all()

    return BaseArticleFilter(filters, qs).qs

def article_get(*, id):
    return Article.objects.get(id=id)