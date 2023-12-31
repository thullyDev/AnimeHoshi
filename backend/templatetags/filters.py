from django import template

register = template.Library()

@register.filter(name='replace')
def replace(value, arg):
    if not isinstance(value, str):
        return value

    old_value, new_value = arg.split(',')
    return value.replace(old_value, new_value)

@register.filter(name='times') 
def times(number):
    return range(1, number + 1)