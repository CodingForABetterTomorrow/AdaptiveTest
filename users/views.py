from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Test, Question
from .forms import RawTest, RawQuestion

from .forms import SignUpForm

def homePage(request):

    return render(request, "users/homepage.html", {})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            print("Form is valid")
            form.save()
            return redirect('/home')
        else:
            print(form.errors)
            print("Form invalid")
    else:
        print("entering else block")
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form, "title": "Sign Up"})


# Create your views here.
def testCreate(request):
    form = RawTest()
    if request.method == "POST":
        form = RawTest(request.POST)
        if form.is_valid():
            Test.objects.create(**form.cleaned_data)
            return redirect('homePage')
    context = {
        "form": form,

    }
    return render(request, "users/createtest.html", context)

def quesCreate(request):
    form = RawQuestion()
    if request.method == "POST":
        form = RawQuestion(request.POST)
        print('hello')
        if form.is_valid():

            Question.objects.create(**form.cleaned_data)
            return redirect('/home')
        else:
            print('invalid')
    context = {
        "form": form,

    }
    return render(request, "users/createtest.html", context)

