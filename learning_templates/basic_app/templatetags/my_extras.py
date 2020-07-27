from django import template

register = template.Library()

def chop(value,arg):
    """"
    This cuts out all values of "arg" from the string!
    """"
    return value.replace(arg,'')

# Register the filter
register.filter("chop", chop) ## register.filter("desiredName", functionName)