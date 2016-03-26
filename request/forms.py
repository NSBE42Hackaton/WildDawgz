from django import forms
from django.forms import TextInput, Textarea  
from .models import RequestParams

class RequestParamsForm(forms.ModelForm):
	class Meta:
		model = RequestParams
		fields = ['first_Name', 'last_Name', 'OS', 'device', 'need', 'software', 'grade', 'gender', 'ethnicity', 'zip_Code'] 