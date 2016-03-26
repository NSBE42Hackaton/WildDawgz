from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib.auth.models import User


def home(request):
	username = None
	if request.user.is_authenticated():
		username = request.user.username
		return render(request, "homepage.html")
		# return redirect( "/%s" % username )
	else:	
		return render(request, "index.html")

def start(request):
	username = None
	if request.user.is_authenticated():
		username = request.user.username
		return render(request, "homepage.html")
		# return redirect( "/%s" % username )
	else:	
		return render(request, "index.html")