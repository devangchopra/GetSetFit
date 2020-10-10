from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import FitmeForm
from .models import Item , Food_Consumed, Image_for_ML
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from django.http import HttpResponse 
from .forms import search_img 

from model_final import ModelPredictor

def home(request):
    return render(request, 'fitme/home.html')



class createfitme(LoginRequiredMixin, CreateView):
    model = Food_Consumed
    fields = ['items','Amount']
    template_name = "fitme/createfitme.html"
    URL = 'currentfitmes'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # def get_success_url(self):
    #     return redirect('currentfitmes')


class search(LoginRequiredMixin, CreateView):
    model = Image_for_ML
    fields = ['image']
    print("This is inside the search class")
    template_name = "fitme/createfitme.html"

    def form_valid(self, form):
        print("This is inside the search function") 
        form.instance.user = self.request.user
        return super().form_valid(form)
     

# Create your views here. 
# def image_view(request):
#     if request.method == 'POST':
#         form = search_img(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             predict = ModelPredictor.ml_search(image_path="/django_fit/media/ml_pics/images.jpg") 
#             print("Predict : ",predict)
#             return redirect('success')
#         else:
#             form = search_img()
#         return render(request, 'fitme/search.html', {'form' : form})
    
#     else:
#         return render(request, 'fitme/search.html')

def image_view(request): 
    if request.method == 'POST': 
        form = search_img(request.POST, request.FILES) 
        if form.is_valid(): 
            print('+++++++++++++',form.instance.image)
            form.save()
            import os
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            print(BASE_DIR)
            predict = ModelPredictor.ml_search(image_path=BASE_DIR+"/media/"+str(form.instance.image)) 
            print("+-+-+--+-+-+-+-+-+-+-  Predict : ",predict)
            data = Item()
            print(data.__dict__)
            return render(request, 'fitme/result.html', {'predict':predict})
    else: 
        form = search_img() 
    return render(request, 'fitme/search.html', {'form' : form}) 






 
@login_required
def currentfitmes(request):
    fitmes = Food_Consumed.objects.filter(user=request.user)
    return render(request, 'fitme/currentfitmes.html', {'fitmes':fitmes})

class consumed(ListView):
    model = Food_Consumed
    template_name = 'fitme/consumed.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'foods'
    paginate_by = 10

    def get_queryset(self):
        return Food_Consumed.objects.filter(user=self.request.user)





@login_required
def completedfitmes(request):
    fitmes = Food_Consumed.objects.filter(user=request.user, time__isnull=False).order_by('-time')
    return render(request, 'fitme/completedfitmes.html', {'fitmes':fitmes})

@login_required
def viewfitme(request, fitme_pk):
    fitme = get_object_or_404(Item, pk=fitme_pk, user=request.user)
    if request.method == 'GET':
        form = FitmeForm(instance=fitme)
        return render(request, 'fitme/viewfitme.html', {'fitme':fitme, 'form':form})
    else:
        try:
            form = FitmeForm(request.POST, instance=fitme)
            form.save()
            return redirect('currentfitmes')
        except ValueError:
            return render(request, 'fitme/viewfitme.html', {'fitme':fitme, 'form':form, 'error':'Bad info'})

@login_required
def completefitme(request, fitme_pk):
    fitme = get_object_or_404(Item, pk=fitme_pk, user=request.user)
    if request.method == 'POST':
        fitme.datecompleted = timezone.now()
        fitme.save()
        return redirect('currentfitmes')

@login_required
def deletefitme(request, fitme_pk):
    fitme = get_object_or_404(Item, pk=fitme_pk, user=request.user)
    if request.method == 'POST':
        fitme.delete()
        return redirect('currentfitmes')

