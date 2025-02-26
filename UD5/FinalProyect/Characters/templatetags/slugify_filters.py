from django import template
from django.utils.text import slugify  

# Registrar los filtros personalizados
register = template.Library()

@register.filter(name='slugify') 
def slugify_filter(value):
    return slugify(value)