from django.shortcuts import render,redirect
from customer import forms
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def customersignup(request):
    form=forms.CustomerRegistrationForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        else:
            return render(request,"customer/signup.html",{"form":form})

    return render(request,"customer/signup.html",context)

def customersignin(request):
    form=forms.LoginAddform()
    context={"form":form}
    if request.method=="POST":
        form=forms.LoginAddform(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return render(request, "customer/mainview.html")
        # else:
        #     return render(request, "customer/signin.html", {"form":form})
    return render(request,"customer/signin.html",context)

def signout(request):
    logout(request)
    return redirect('signin')
