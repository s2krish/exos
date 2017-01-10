from random import randint

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext as _

from .models import UserProfile


class UserProfileCreationForm(UserCreationForm):
    # random_number = forms.IntegerField()
    birthday = forms.DateField(
        help_text=_("In YYYY-MM-DD format"),
        widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=commit)
        user_profile = UserProfile.objects.create(
            user=user,
            birthday=self.cleaned_data['birthday'],
            random_number=randint(1, 100),
            )

        return user_profile
