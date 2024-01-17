from django import template
import ast

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

@register.filter(name='safebool') 
def safebool(value):
    hashmap = {
        False: "false",
        True: "true"
    }
    
    return hashmap.get(value, value)

@register.filter(name='safe_list') 
def safe_list(value):
    return ast.literal_eval(value)