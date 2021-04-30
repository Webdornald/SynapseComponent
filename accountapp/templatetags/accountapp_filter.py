import markdown
from django import template
from time import time
from django.conf import settings
from django.templatetags.static import StaticNode
from django.utils.safestring import mark_safe

register = template.Library()


class FreshStaticNode(StaticNode):
    def url(self, context):
        url = super().url(context)
        if settings.DEBUG:
            url += '?_={}'.format(int(time()))
        return url


@register.tag('fresh_static')
def do_static(parser, token):
    return FreshStaticNode.handle_token(parser, token)


@register.filter
def sub(value, arg):
    return value - arg


@register.filter
def mark(value):
    extensions = ['nl2br', 'fenced_code']
    return mark_safe(markdown.markdown(value, extensions=extensions))