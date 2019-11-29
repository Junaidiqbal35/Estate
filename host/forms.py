from django import forms

from host.models import Host


class userProfileForm(forms.ModelForm):

    class Meta:
        model = Host
        field ="__all__"



