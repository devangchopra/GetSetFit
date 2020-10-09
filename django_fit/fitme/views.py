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

def home(request):
    return render(request, 'fitme/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'fitme/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentfitmes')
            except IntegrityError:
                return render(request, 'fitme/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'fitme/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'fitme/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'fitme/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('currentfitmes')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')



class createfitme(LoginRequiredMixin, CreateView):
    model = Food_Consumed
    fields = ['items','Amount']
    template_name = "fitme/createfitme.html"
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class search(LoginRequiredMixin, CreateView):
    model = Image_for_ML
    fields = ['image']
    template_name = "fitme/createfitme.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
     

# Create your views here. 
def image_view(request): 

	if request.method == 'POST': 
		form = search_img(request.POST, request.FILES) 

		if form.is_valid(): 
			form.save() 
			return redirect('success') 
	else: 
		form = search_img() 
	return render(request, 'fitme/search.html', {'form' : form}) 


def success(request): 
	return HttpResponse('successfully uploaded') 





@login_required
def currentfitmes(request):
    fitmes = Food_Consumed.objects.filter(user=request.user, time__isnull=True)
    return render(request, 'fitme/currentfitmes.html', {'fitmes':fitmes})

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

