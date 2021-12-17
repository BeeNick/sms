from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from smsUI.forms import smsUIUserCreationForm


#main hompage
def home(request):
	return render(request, 'home.html')


#main personal user hompage
def personalHome(request):
	return render(request, 'personalHome.html')


#new user registrantion page
def register(request):

	if request.method == 'GET':
		return render(
			request, 'register.html',
			{'form': smsUIUserCreationForm}
		)

	elif request.method == 'POST':
		form = smsUIUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect(reverse('personalHome'))

	return redirect(reverse('home'))

