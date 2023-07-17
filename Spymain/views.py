from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from Spymain.models import  Models_info as Details
from Spymain.models import  model_assets as Tags
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .forms import SignUpForm,LoginForm


def index(request):
    data = Details.objects.all()
    context={
        'model':data,
    }
    demo=User.objects.all()
    return render(request,'index.html',context)

def navigation(request):
    # User_info=User.objects.all()
    # if request.method=="GET":
    #     form = LoginForm(request.GET)
    #     if form.is_valid():
    #         perfect_password = form.cleaned_data.get('password')
    #         user = authenticate(username=user.username, password=perfect_password)
    #         login(request, user)
    #     else:
    #         form=form = LoginForm(request.GET)
    return render(request,'index.html')

def test(request):
    return render(request,'test.html')


 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

