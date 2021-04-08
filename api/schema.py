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
        This resolver (union type with this block case) below _should_ work, if we give it some
        data to return

        self should be (is) a BlogPage instance. The other fields exist.
        I'm expecting all the data from the db record should be available here, but this is where
        my knowledge of Django/Wagtail fails me.

        Some examples use self.body.stream_data, however this is deprecated in favour of just using
        self.body. I've tried both, they're both an empty StreamField list.
        """
        repr_body = []
        for block in self.body:
            block_type = block.block_type
            value = block.value
            if block_type == 'paragraph':
                repr_body.append(ParagraphBlock(value=value.source))
            elif block_type == 'heading':
                repr_body.append(HeadingBlock(value=value))
        return repr_body


class Query(graphene.ObjectType):
    articles = graphene.List(ArticleNode)

    def resolve_articles(root, info, **kwargs):
      return BlogPage.objects.all()

schema = graphene.Schema(query=Query)
