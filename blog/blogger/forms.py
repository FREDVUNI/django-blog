from django import forms
from .models import Blogger

class contactForm(forms.Form):
    fullname = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get("email")
        
        #qs = Blogger.objects.filter(email__iexact = email) #can also use email__icontains
        if email.endswith(".edu"):
            raise forms.ValidationError("The email cannot end with edu")
        return email
        #if qs.exists():
        #    raise forms.ValidationError("Email address already exists")

