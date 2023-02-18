from django import template

register = template.Library()

def my_filter(value):
    return value + ' ' + 'Hello'

register.filter('Custom_filter', my_filter)