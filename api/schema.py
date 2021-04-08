from __future__ import unicode_literals
import graphene
from graphene_django import DjangoObjectType
from blog.models import BlogPage
from graphene.types.generic import GenericScalar

from django.db import models

# from api import graphene_wagtail

class ParagraphBlock(graphene.ObjectType):
    value = GenericScalar()

class HeadingBlock(graphene.ObjectType):
    value = GenericScalar()

class BlogPageBody(graphene.Union):
    class Meta:
      types = (ParagraphBlock, HeadingBlock)


class ArticleNode(DjangoObjectType):
    body = graphene.List(BlogPageBody)

    class Meta:
        model = BlogPage
        fields = ('id', 'title', 'date', 'intro')

    def resolve_body(self, info):
      """
      self.body seems to be an empty list, but from frontend test, definitely contains data
      """
        repr_body = []
        for block in self.body:
            block_type = block.get('type')
            value = block.get('value')
            if block_type == 'paragraph':
                repr_body.append(ParagraphBlock(value=value))
            elif block_type == 'heading':
                repr_body.append(HeadingBlock(value=value))
        return repr_body


class Query(graphene.ObjectType):
    articles = graphene.List(ArticleNode)

    def resolve_articles(root, info, **kwargs):
      return BlogPage.objects.all()

schema = graphene.Schema(query=Query)
