# custom_filters.py
from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (TypeError, ValueError):
        return value
    
@register.filter(name='sum')
def sum_values(value, arg):
    try:
        return float(value) + float(arg)
    except (TypeError, ValueError):
        return value