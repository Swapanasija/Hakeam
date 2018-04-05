from django import forms
from myapp.models import Donor,Acceptor,Help

class DonorForm(forms.ModelForm):
    class Meta():
        model = Donor
        fields = ['name','blood_group','dob','gender','phone','email_id','medicalHistory','location']

class AcceptorForm(forms.ModelForm):
    class Meta():
        model = Acceptor
        fields = ['name','blood_group','dob','gender','phone','email_id','medicalHistory','location']

class HelpForm(forms.ModelForm):
    class Meta():
        model = Help
        fields = '__all__'
