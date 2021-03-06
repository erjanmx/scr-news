from .config import Model
from orator.orm import belongs_to_many

class Tag(Model):
    __timestamps__ = False
    __fillable__ = ['name']


class Article(Model):
    __timestamps__ = False
    __fillable__ = ['source_id', 'url', 'title']

    @belongs_to_many
    def tags(self):
        return Tag


class ArticlesTags(Model):
    __timestamps__ = False
    __fillable__ = ['article_id', 'tag_id']


class ArticlesBody(Model):
    __timestamps__ = False
    __table__ = 'articles_bodies'
    __fillable__ = ['article_id', 'content']
