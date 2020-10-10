from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect


 
class Item(models.Model):
    Name = models.CharField(max_length=100,  primary_key=True)
    Calories = models.IntegerField()
    Carbohydrate = models.IntegerField()
    Fiber = models.IntegerField()
    Fats = models.IntegerField()
    def __str__(self):
        return self.Name
    
class Image_for_ML(models.Model):
    image = models.ImageField(upload_to='ml_pics')

    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.image.url)



class Food_Consumed(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    Amount = models.IntegerField()

    def get_cart_items(self):
        return self.items.all()

    def get_calories_total(self):
        return sum([item.Item.Calories for item in self.items.all()])
        
    # def get_absolute_url(self):
    #     return redirect('currentfitmes')
    # def get_absolute_url(self):
    #     return reverse('viewfitme', kwargs={'pk': self.pk})
    

