from django.contrib import admin
from .models import Item, Food_Consumed, Image_for_ML

admin.site.register(Item)
admin.site.register(Food_Consumed)
admin.site.register(Image_for_ML)

