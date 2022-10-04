from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse
from demo.models import Signup
from demo.models import Signup2
from demo.forms import SignupForm, SignupForm2


def index(request):
    detail = Signup.objects.all()
    return render(request, 'index.html',{'data':detail})

def add(request):
    if request.method =="POST":
        form = SignupForm(request.POST)
        def clean_password_confirm(self):
            password = self.cleaned_data['password']
            password_confirm = self.cleaned_data.get('confirm_password')
            if password and password_confirm:
                if password != password_confirm:
                    raise form.ValidationError("The two password fields must match.")
            return password_confirm
        if form.is_valid():
            form.save()
            return redirect('read')
    else:
        form = SignupForm

    context = {
        'form': form
    }
    return render(request, 'signup.html',context)
   
def signin(request):
    if request.method =="POST":
        form = SignupForm2(request.POST)
        def clean_password_confirm(self):
            password = self.cleaned_data['password']
            password_confirm = self.cleaned_data.get('confirm_password')
            if password and password_confirm:
                if password != password_confirm:
                    raise form.ValidationError("The two password fields must match.")
            return password_confirm
        if form.is_valid():
            form.save()
            return redirect("read")
    else:
        form = SignupForm2

    context = {
        'form': form
    }
    return render(request,"signup2.html",context)

def login(request):
    return render(request,"login.html")











