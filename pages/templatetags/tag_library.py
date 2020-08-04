from django import template

register = template.Library()


@register.filter()
def to_int(value):
    return int(float(value))


@register.filter()
def to_list(value):
    return value.split(",")
