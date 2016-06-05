from __future__ import absolute_import, unicode_literals

from wagtail.wagtailcore.models import Page
from django.db import models
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class HomePage(Page):
    name = models.CharField(max_length=255)
    about = RichTextField(max_length=1000)

    content_panels = Page.content_panels + [
        FieldPanel('name', classname="full"),
        FieldPanel('about', classname="full"),
    ]
