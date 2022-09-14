from django import forms
from django.core import validators
from first_app.models import User as user_app
from first_app.models import User_info
from django.contrib.auth.models import User



def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name must start with z!")


class FormName(forms.Form):
    name = forms.CharField(label='Name', validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxValueValidator('')])  # 防止机器人

    '''def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("Catch Bot!")
        return botcatcher'''

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")


class NewUser(forms.ModelForm):
    class Meta():
        model = user_app
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class User_profile(forms.ModelForm):
    class Meta():
        model = User_info
        fields = ('portfolio_site', 'profile_pic')