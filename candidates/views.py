from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from users.models import Test
from .forms import CandidateRegisterForm
# Create your views here.
def showrules(request,*args,**kwargs):
	context={}
	return render(request, "candidates/rules.html", context)
def candidatesignin_view(request,*args,**kwargs):
	my_form = CandidateRegisterForm()
	if request.method == "POST":
		my_form = CandidateRegisterForm(request.POST)
		if my_form.is_valid():
			x=request.POST.get('testid')
			y=request.POST.get('testpassword')

			if Test.objects.filter(TestID=x).exists():
				query=Test.objects.get(TestID=x)
				if query.passwd==y:
					print(my_form.cleaned_data)
					Student.objects.create(**my_form.cleaned_data)
					return redirect('/rules')
				else:
					print('wrong pasword')
			else:
				print("Does not exist")


	else:
		my_form=CandidateRegisterForm(request.POST)
	context={
		"form": my_form
	}
	#return HttpResponse("<h1>Hello Candidate<h1>")
	return render(request,"candidates/candidatesignin.html",context)