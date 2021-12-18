from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	location = models.CharField(max_length=30, blank=True)
	slug = models.SlugField(max_length = 250, null=True, blank=True)

	class Meta:
		ordering = ['user']
		constraints = [models.UniqueConstraint(fields=['user'], name='unique_user_profile')]

	def __str__(self):
		return self.user.username


# Define skills set class, example: "Programming Languages"
class SkillsSet(models.Model):
	skills_set_name = models.CharField(max_length=50)

	class Meta:
		ordering = ['skills_set_name']
		constraints = [models.UniqueConstraint(fields=['skills_set_name'], name='unique_skills_set')]

	def __str__(self):
		return self.skills_set_name


# Define skill element class, example: in skills set "Programming Languages" a skill element can be Python 
class SkillElement(models.Model):
	skill_element_name = models.CharField(max_length=50)
	skill_set = models.ForeignKey(SkillsSet, on_delete=models.CASCADE)

	class Meta:
		ordering = ['skill_set', 'skill_element_name']
		constraints = [models.UniqueConstraint(fields=['skill_element_name'], name='unique_skill_element')]

	def __str__(self):
		return f'skills set: {self.skill_set.skills_set_name} - element: {self.skill_element_name}'


# Define association between skill elements and userProfiles
class PersonalSkills(models.Model):
	user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	skill_element = models.ForeignKey(SkillElement, on_delete=models.CASCADE)
	familiarity = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])

	class Meta:
		ordering = ['user_profile', '-familiarity', 'skill_element__skill_set', 'skill_element']
		constraints = [models.UniqueConstraint(fields=['user_profile','skill_element'], name='unique_personal_skills')]

	def __str__(self):
		return f'user: {self.user_profile.user.username} - skills set: {self.skill_element.skill_set} \
		 element: {self.skill_element.skill_element_name} - familiarity: {self.familiarity}/5'



    