from django import template

register = template.Library()

@register.filter
def percentage(value):
    return value  # Assuming the total_mark is out of 20