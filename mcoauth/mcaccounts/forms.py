from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import MinecraftAccount
from .authenticate import authenticate

class MinecraftAccountForm(forms.ModelForm):
    password = forms.CharField(
        label=_('Password'),
        help_text=_('Your password will not be stored in our database'),
        widget=forms.PasswordInput)

    class Meta:
        model = MinecraftAccount
        fields = ('name',)

    def clean(self):
        cleaned_data = super(MinecraftAccountForm, self).clean()

        username = self.cleaned_data.get('name')
        password = self.cleaned_data.get('password')

        try:
            authenticate(username, password)
        except:
            raise forms.ValidationError(_(
                'You entered invalid credentials. '
                'Username or password are incorrect.'))

        return cleaned_data

    def save(self, user, **kwargs):
        self.instance.user = user
        return super(MinecraftAccountForm, self).save(**kwargs)
