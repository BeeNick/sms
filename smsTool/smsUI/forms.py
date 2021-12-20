from django.contrib.auth.forms import UserCreationForm
from django import forms
from smsUI.models import PersonalSkills, SkillElement, SkillsSet, UserProfile, Seniority
from django.utils.timezone import now


class smsUIUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class EditPersonalSkillsForm(forms.Form):
    # bad use of try except, only to speed up development
    # TODO: remove try except

    try:
        for index, skill in enumerate(SkillElement.objects.all()):
            # wrong way: only the label has the value of the element, the filed is enumerative
            exec(f"skill_{index} = \
             forms.IntegerField( label='{skill.skill_set.name} - {skill.name} familiarity: ', \
              min_value=0, max_value=5)")
    except Exception as e:
        print('Edit personal skills form error')
        print(e)
        #TODO : manage try errors

    def __init__(self, user=None, *args, **kwargs):
        super(EditPersonalSkillsForm, self).__init__(*args, **kwargs)

        personal_skills = PersonalSkills.objects.filter(
                user_profile=UserProfile.objects.get(user=user)
            )

        try:        
            for index, skill in enumerate(SkillElement.objects.all()):
                for personal_skill in personal_skills:
                    if skill.name == personal_skill.skill_element.name:
                        exec(f"self.fields['skill_{index}'].initial = {personal_skill.familiarity}")

        except Exception as e:
            print('Edit personal skills form initialization error')
            print(e)
            #TODO : manage try errors
 

class NewSkillElementForm(forms.Form):
    skill_set = forms.ModelChoiceField(queryset=SkillsSet.objects.all(), label='Skill set: ')
    name = forms.CharField(label='Skill element: ', widget=forms.TextInput(attrs={'size': 50}))
    # Considering that the new skill element page will be visible from edit skills from the personal hompage
    # is more user friendly allow to add directly the familiarity value for the new skill element directly in this form
    familiarity = forms.IntegerField(label='Familiarity: ', min_value=0, max_value=5)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['skill_set'].queryset = SkillsSet.objects.all()
        self.fields['familiarity'].initial = 0
        try:
            # Considering the case skillsSet hasn't been defined yet
            self.fields['skill_set'].initial = SkillsSet.objects.all()[0]
        except Exception as e:
            print(e)


class NewSkillsSetForm(forms.Form):
    name = forms.CharField(label='Skill element: ', widget=forms.TextInput(attrs={'size': 50}))


# Using model Form for user profile we have the problem of limiting the user choicefield for the logget user
# due to this I'm using a normal manually specified form
class EditUserProfileForm(forms.Form):
    joining_date = forms.DateField(label='Joining date: ')
    role = forms.CharField(label='Role: ', widget=forms.TextInput(attrs={'size': 100}))
    seniority = forms.ModelChoiceField(queryset=Seniority.objects.all(), label='Seniority: ', required=False)
    location = forms.CharField(label='Location: ', widget=forms.TextInput(attrs={'size': 30}), required=False)
    bio = forms.CharField(label='Bio: ', widget=forms.TextInput(attrs={'size': 600}), required=False)

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        try:
            user_profile = UserProfile.objects.get(user=user)
            self.fields['role'].initial = user_profile.role
            self.fields['seniority'].initial = user_profile.seniority
            self.fields['joining_date'].initial = user_profile.joining_date
            self.fields['bio'].initial = user_profile.bio
            self.fields['location'].initial = user_profile.location
        except Exception as e:
            print(e)
            self.fields['joining_date'].initial = now().today()





