from django.contrib.auth.forms import UserCreationForm
from django import forms
from smsUI.models import PersonalSkills, SkillElement, SkillsSet


class smsUIUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class EditPersonalSkillsForm(forms.Form):
    # bad use of try except, only to speed up development
    # TODO: remove try except

    try:
        for index, skill in enumerate(SkillElement.objects.all()):
            # wrong way: only the label has the value of the element, the filed is enumerative
            exec(f"skill_{index} = forms.PositiveIntegerField(\
                label='{skill.skill_set.name} - {skill.name} familiarity: ')")
    except Exception as e:
        print('Edit personal skills form error')
        print(e)
        #TODO : manage try errors

    def __init__(self, user=None, *args, **kwargs):
        super(EditPersonalSkillsForm, self).__init__(*args, **kwargs)

        try:
            personal_skills = PersonalSkills.objects.filter(user=user)
        
            for index, skill in enumerate(SkillElement.objects.all()):
                exec(f"self.fields['skill_{index}'].initial = \
                    {PersonalSkills.objects.get(user=user, skill_element=skill).familiarity}")

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

    def __init__(self, socialclass_id=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['skill_set'].queryset = SkillsSet.objects.all()
        self.fields['familiarity'] = 0
        try:
            # Considering the case skillsSet hasn't been defined yet
            self.fields['skill_set'].initial = SkillsSet.objects.all()[0]
        except Exception as e:
            print(e)


class NewSkillsSetForm(forms.Form):
    name = forms.CharField(label='Skill element: ', widget=forms.TextInput(attrs={'size': 50}))






