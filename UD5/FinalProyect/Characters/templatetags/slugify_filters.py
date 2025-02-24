from django import template
from django.utils.text import slugify  # Importamos slugify para convertir el texto

# Registrar los filtros personalizados
register = template.Library()

@register.filter(name='slugify')  # Decorador para registrar el filtro
def slugify_filter(value):
    return slugify(value)