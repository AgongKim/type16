from rest_framework import request
from type16.models import Article, User

class ArticleService():

    def __init__(self, request:request) -> None:
        self.request = request

    def create(self,
        category: str,
        title: str,
        content: str,
        user: User,
        is_viewable: str,
        hits: int,  
    ) -> Article:
        article = Article(
            category=category,
            title=title,
            content=content,
            user=user,
            is_viewable=is_viewable,
            hits=hits)
        article.save()
        return article