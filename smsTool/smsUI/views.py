from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from django.views.generic import DetailView, ListView
from smsUI.forms import smsUIUserCreationForm
from smsUI.models import PersonalSkills, UserProfile


#main hompage
def home(request):
	return render(request, 'home.html')

# Class based list view for personal Hompage based on personal skills model (wrong way)
class personalHome_shortcut(ListView):
	model = PersonalSkills
	context_object_name = 'skills_list'
	template_name = 'personalHome2.html'

	def get_queryset(self): 
		return PersonalSkills.objects.filter(user_profile__user=self.request.user)

# Class based detail view for personal Hompage based on UserProfile (good way with slug definition problems)
class personalHome(DetailView):
	model = UserProfile
	context_object_name = 'profile'
	template_name = 'personalHome.html'

	def get_queryset(self): 
		return UserProfile.objects.filter(user=self.request.user)


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

