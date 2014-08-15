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
            response = authenticate(username, password)
        except:
            raise forms.ValidationError(_(
                'You entered invalid credentials. '
                'Username or password are incorrect.'))
        else:
            selected_profile = response.get('selectedProfile')

            profile_id = selected_profile.get('id')
            profile = selected_profile.get('name')

            self.instance.profile_id = profile_id
            self.instance.profile = profile

            try:
                MinecraftAccount.objects.get(profile_id=profile_id)
            except MinecraftAccount.DoesNotExist:
                pass
            else:
                raise forms.ValidationError(_(
                    'This Minecraft Profile is already being used '
                    'by another account.'))

        return cleaned_data

    def save(self, user, **kwargs):
        self.instance.user = user
        return super(MinecraftAccountForm, self).save(**kwargs)
