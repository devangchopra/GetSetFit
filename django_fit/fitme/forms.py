from django.forms import ModelForm
from .models import Item , Image_for_ML

class FitmeForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

  
class search_img(ModelForm): 
  
    class Meta: 
        model = Image_for_ML 
        fields = '__all__' 