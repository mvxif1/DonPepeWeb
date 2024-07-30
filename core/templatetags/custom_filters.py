# core/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def format_clp(value):
    try:
        return "${:,.0f}".format(value)
    except (ValueError, TypeError):
        return value

@register.filter
def multiplicar(value, arg):
    try:
        return value * arg
    except (TypeError, ValueError):
        return 0
