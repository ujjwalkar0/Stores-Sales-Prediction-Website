from django import template

register = template.Library()

@register.filter
def remove_(value):
    return value.replace("_"," ")
