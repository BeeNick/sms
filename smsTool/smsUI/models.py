from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.utils.timezone import now

# Define seniority class, example: "Junior developer -> Junior"
class Seniority(models.Model):
	name = models.CharField(max_length=50)
	rank = models.PositiveIntegerField(null=True)

	class Meta:
		ordering = ['-rank','name']
		constraints = [models.UniqueConstraint(fields=['name'], name='unique_seniority_name'), \
		models.UniqueConstraint(fields=['rank'], name='unique_seniority_rank')]

	def __str__(self):
		return f'{self.name} {self.rank}'


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	role = models.TextField(max_length=100, blank=True)
	seniority = models.ForeignKey(Seniority, on_delete=models.CASCADE, null=True)
	joining_date = models.DateField(default=now().today(), blank=True)
	bio = models.TextField(max_length=600, blank=True)
	location = models.CharField(max_length=30, blank=True)
	slug = models.SlugField(max_length = 250, null=True, blank=True)

	class Meta:
		ordering = ['user']
		constraints = [models.UniqueConstraint(fields=['user'], name='unique_user_profile')]

	def __str__(self):
		return self.user.username


# Define skills set class, example: "Programming Languages"
class SkillsSet(models.Model):
	name = models.CharField(max_length=50)

	class Meta:
		ordering = ['name']
		constraints = [models.UniqueConstraint(fields=['name'], name='unique_skills_set')]

	def __str__(self):
		return self.name


# Define skill element class, example: in skills set "Programming Languages" a skill element can be Python 
class SkillElement(models.Model):
	name = models.CharField(max_length=50)
	skill_set = models.ForeignKey(SkillsSet, on_delete=models.CASCADE)

	class Meta:
		ordering = ['skill_set', 'name']
		constraints = [models.UniqueConstraint(fields=['name'], name='unique_skill_element')]

	def __str__(self):
		return f'( skills set: {self.skill_set.name} - element: {self.name} )'


# Define association between skill elements and userProfiles
class PersonalSkills(models.Model):
	user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	skill_element = models.ForeignKey(SkillElement, on_delete=models.CASCADE)
	familiarity = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])

	class Meta:
		ordering = ['user_profile', '-familiarity', 'skill_element__skill_set', 'skill_element']
		constraints = [models.UniqueConstraint(fields=['user_profile','skill_element'], name='unique_personal_skills')]

	def __str__(self):
		return f'( user: {self.user_profile.user.username} - skills set: {self.skill_element.skill_set} \
		 element: {self.skill_element.name} - familiarity: {self.familiarity}/5 )'



    