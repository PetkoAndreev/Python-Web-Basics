from django import forms

from expenses_tracker.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name')


class CreateProfileForm(ProfileForm):
    pass


class EditProfileForm(ProfileForm):
    pass
