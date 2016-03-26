from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect

from .forms import RequestParamsForm
from .models import RequestParams

def submit_request(request):
	username = None
	if request.user.is_authenticated():
		username = request.user.username
		
		form = RequestParamsForm(request.POST or None)
		status = "<h2><font color='green'>You have already completed this form.</font></h2> <h3>To update your information please resubmit the form.</h3> "
		context = {
			"form": form,
			"status": status
		}
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user_Name = username
			instance.first_Name = form.cleaned_data['first_Name']
			instance.last_Name = form.cleaned_data['last_Name']
			instance.OS = form.cleaned_data['OS']
			instance.device = form.cleaned_data['device']
			instance.need = form.cleaned_data['need']
			instance.software = form.cleaned_data['software']
			instance.grade = form.cleaned_data['grade']
			instance.gender = form.cleaned_data['gender']
			instance.ethnicity = form.cleaned_data['ethnicity']
			instance.zip_Code = form.cleaned_data['zip_Code']
			instance.save()
			return redirect( "/start")

		else:	
			return render(request, "searchparam.html", context)	
	else:
		return render(request, "index.html")
