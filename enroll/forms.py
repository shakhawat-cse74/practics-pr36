from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
   
    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']

        if len(valname) < 4 :
            raise forms.ValidationError('Enter more than 4 or equal')

        if len(valemail) < 10 :
            raise forms.ValidationError('Enter more than 10 or equal')
