from django.contrib.auth.forms import UserCreationForm

class smsUIUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)