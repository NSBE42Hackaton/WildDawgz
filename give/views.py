from django.conf import settings
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from request.models import RequestParams

def show_request(request):
	username = None
	if request.user.is_authenticated():
		username = request.user.username
		queryset = RequestParams.objects.all()
		context = {
				"object_list": queryset,
				"title": "List",
		}

		# res = RequestParams.objects.values_list('OS', 'device')
		# data = {'OS' : res}
		# context = "name" 

		return render(request, "results.html", context)
	else:
		return render(request, "profile.html")
	# username = None
	# if request.user.is_authenticated():
	# 	username = request.user.username
	# 	context = dict()
	# 	context['results'] = RequestParams.objects.all()
	# 	return render(request, "results.html", context)
	# else:
	# 	return render(request, "profile.html")

def detail(request, id):
	username = None
	if request.user.is_authenticated():
		instance = get_object_or_404(RequestParams, id=id)
		context = {
				"name": instance.user_Name,
				"instance": instance,
		}

		return render(request, "dets.html", context)
	else:
		return render(request, "profile.html")
