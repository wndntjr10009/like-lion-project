from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def signup(request):
    context=dict()
    signup_form=UserCreationForm()
    context['signup_form']=signup_form
    return render(request, 'signup.html',context)