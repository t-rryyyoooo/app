from django import template
from .models import 

register = template.Library()

@register.filter
def value(part):

