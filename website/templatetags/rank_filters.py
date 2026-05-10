from django import template

register = template.Library()

@register.filter
def abs_rank_class(value):
    """Convert ABS rank to CSS class name."""
    if not value:
        return ''
    if value == '4*':
        return 'rank-abs-4star'
    elif value == '4':
        return 'rank-abs-4'
    elif value == '3':
        return 'rank-abs-3'
    elif value == '2':
        return 'rank-abs-2'
    elif value == '1':
        return 'rank-abs-1'
    return ''

@register.filter
def sjr_rank_class(value):
    """Convert SJR rank to CSS class name."""
    if not value:
        return ''
    return f'rank-sjr-{value.lower()}'
