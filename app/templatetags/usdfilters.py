from django import template

register=template.Library()

def swapping(value):
    return value.swapcase()
def remove(value,arg):
    return value.replace(arg,'')

    register.filter('swapping',swapping)
    register.filter('remove',remove)