from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

def index(request):
   return render(request, 'main/index.html')

def other_page(request, page):
   try:
       template = get_template('main/' + page + '.html')
   except TemplateDoesNotExist:
       raise Http404
   return HttpResponse(template.render(request=request))

@login_required
def profile(request):
   return render(request, 'main/profile.html')

class BBLoginView(LoginView):
   template_name = 'main/login.html'


# Create your views here.
