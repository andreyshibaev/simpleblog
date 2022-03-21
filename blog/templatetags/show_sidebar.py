from multiprocessing import context
from blog.models import CategoryPost
from django import template

register = template.Library()



@register.inclusion_tag('blog/show_sidebar.html')
def show_categories():
   categories = CategoryPost.objects.all()
   return {'categories': categories}