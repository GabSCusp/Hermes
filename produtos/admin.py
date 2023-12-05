from django.contrib import admin

from .models import Produto, Review, List 

admin.site.register(Produto)
admin.site.register(Review)
admin.site.register(List)