from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from django.views.generic import DetailView, ListView
from smsUI.forms import smsUIUserCreationForm, EditPersonalSkillsForm
from smsUI.models import PersonalSkills, UserProfile, SkillElement


# Main hompage
def home(request):
	return render(request, 'home.html')

# Class based list view for personal hompage based on PersonalSkills model (wrong way, but working)
class personalHome_shortcut(ListView):
	model = PersonalSkills
	context_object_name = 'skills_list'
	template_name = 'personalHome2.html'

	def get_queryset(self): 
		return PersonalSkills.objects.filter(user_profile__user=self.request.user)

# Class based detail view for personal hompage based on UserProfile (good way, with slug definition problems)
class personalHome(DetailView):
	model = UserProfile
	context_object_name = 'profile'
	template_name = 'personalHome.html'

	def get_queryset(self): 
		return UserProfile.objects.filter(user=self.request.user)


# New user registrantion page
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


# Edit personal skills
def editPersonalSkills(request):

	form = EditPersonalSkillsForm(user=request.user)  # Init the form with user values
	if request.method == 'POST':
		# Parse data from the POST in form_data
		form_data = EditPersonalSkillsForm(user=request.user, data=request.POST)
		if form_data.is_valid():   
			for index, skill in enumerate(SkillElement.objects.all()):
				personal_skill = PersonalSkills.objects.get(user=request.user, skill_element=skill)
				personal_skill.familiarity = form_dati.cleaned_data[f'skill_{i}']
				personal_skill.save()

			print("Personal skills editing completed")

			return redirect(reverse('personalHome'))

		else:
			return render(request, "editPersonalSkills.html", {"form": form}, \
				{"error_message": "Something wrong in editing skills"})

	else:
		print("GET")
		return render(request, 'editPersonalSkills.html', {"form": form})