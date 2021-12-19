from django.contrib.auth.forms import UserCreationForm
from django import forms
from smsUI.models import PersonalSkills, SkillElement


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
 
