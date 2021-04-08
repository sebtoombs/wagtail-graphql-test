
# Create your models here.
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.search import index
from wagtail.core import blocks

# from grapple.models import (
#     GraphQLString,
#     GraphQLStreamfield,
# )

# class BlogIndexPage(Page):
#     intro = RichTextField(blank=True)

#     content_panels = Page.content_panels + [
#         FieldPanel('intro', classname="full")
#     ]



class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)

    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
    ])

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
    ]


    # graphql_fields = [
    #     GraphQLString("heading"),
    #     GraphQLString("date"),
    #     GraphQLString("author"),
    #     GraphQLStreamfield("body"),
    # ]