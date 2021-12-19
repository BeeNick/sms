from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from django.views.generic import DetailView, ListView
from smsUI.forms import smsUIUserCreationForm, EditPersonalSkillsForm, NewSkillElementForm, NewSkillsSetForm, EditUserProfileForm
from smsUI.models import PersonalSkills, UserProfile, SkillElement, SkillsSet


# Main hompage
def home(request):
	return render(request, 'home.html')

# Class based list view for personal hompage based on PersonalSkills model (wrong way, but working)
class personalHome_shortcut(ListView):
	model = PersonalSkills
	context_object_name = 'skills_list'
	template_name = 'personalHome2.html'

	def get_queryset(self): 
		return PersonalSkills.objects.filter(user_profile=UserProfile.objects.get(user=self.request.user))

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
				personal_skill.familiarity = form_data.cleaned_data[f'skill_{i}']
				personal_skill.save()

			print("Personal skills editing completed")

			return redirect(reverse('personalHome'))

		else:
			return render(request, "editPersonalSkills.html", {"form": form}, \
				{"error_message": "Something wrong in editing skills"})

	else:
		print("GET")
		return render(request, 'editPersonalSkills.html', {"form": form})


# Add new skill element
def addSkill(request):

	form = NewSkillElementForm()  # Init the form with user values
	if request.method == 'POST':
		# Parse data from the POST in form_data
		form_data = NewSkillElementForm(data=request.POST)
		if form_data.is_valid():   
			new_skill_name = form_data.cleaned_data['name']

			#Avoid duplicate skill elements
			try:
				SkillElement.objects.get(name=new_skill_name)
				print("Skill element name already exist!")
				return render(request, "newSkillElement.html", {"form": form}, \
				{"error_message": "Skill element name already exist! Please insert a different name"})
			except:
				# Save new skill element
				new_skill_element = SkillElement()
				new_skill_element.name = new_skill_name
				new_skill_element.skill_set = form_data.cleaned_data['skill_set']
				new_skill_element.save()
				print("Skill element saved")

				# Update user personal skills familiarity for the new skill element
				try:
					personal_skill = PersonalSkills.objects.get(\
						user_profile=UserProfile.objects.get(user=request.user), skill_element=new_skill_element)
					personal_skill.familiarity = form_data.cleaned_data['familiarity']
					personal_skill.save()
					print("User personal skills updated")
					return redirect(reverse('editPersonalSkills'))
				except:
					return render(request, "newSkillElement.html", {"form": form}, \
						{"error_message": \
						"Warning: Skill element saved, having trouble updating user personal skills"})

		else:
			return render(request, "newSkillElement.html", {"form": form}, \
				{"error_message": "Something wrong in adding new skill"})

	else:
		print("GET")
		return render(request, 'newSkillElement.html', {"form": form})


# Add new skills set
def addSkillsSet(request):

	form = NewSkillsSetForm()  
	if request.method == 'POST':
		# Parse data from the POST in form_data
		form_data = NewSkillsSetForm(data=request.POST)
		if form_data.is_valid():   
			new_skills_set_name = form_data.cleaned_data['name']

			#Avoid duplicate skill elements
			try:
				SkillsSet.objects.get(name=new_skills_set_name)
				print("Skills set name already exist!")
				return render(request, "newSkillsSet.html", {"form": form}, \
				{"error_message": "Skills set name already exist! Please insert a different name"})
			except:
				# Save new skills set
				new_skills_set = SkillsSet()
				new_skills_set.name = new_skills_set_name
				new_skills_set.save()
				print("Skills set saved")

				# The insertion of new skills set will be possible only in editing skills
				return redirect(reverse('newSkillElement'))
		else:
			return render(request, "newSkillsSet.html", {"form": form}, \
				{"error_message": "Something wrong in adding new skills set"})

	else:
		print("GET")
		return render(request, 'newSkillsSet.html', {"form": form})


# Edit user profile, allow also save new user profile
def editUserProfile(request):

	form = EditUserProfileForm(user=request.user)  # Init the form with user values
	if request.method == 'POST':
		# Parse data from the POST in form_data
		form_data = EditUserProfileForm(user=request.user, data=request.POST)
		if form_data.is_valid():   
			
			#Avoid duplicate user profile, and allow insertion new user profile
			try:
				# Edit existing user profile
				user_profile = UserProfile.objects.get(user=request.user)
				print("Edit user profile")
			except:
				# New user profile
				user_profile = UserProfile()
				user_profile.user = request.user
				print("New user profile")
			
			finally:
				user_profile.role = form_data.cleaned_data['role']
				user_profile.seniority = form_data.cleaned_data['seniority']
				user_profile.joining_date = form_data.cleaned_data['joining_date']
				user_profile.bio = form_data.cleaned_data['bio']
				user_profile.location = form_data.cleaned_data['location']
				user_profile.save()
				print("User profile saved")
				return redirect(reverse('personalHome'))

		else:
			return render(request, "editUserProfile.html", {"form": form}, \
				{"error_message": "Something wrong in editing user profile"})

	else:
		print("GET")
		return render(request, 'editUserProfile.html', {"form": form})
