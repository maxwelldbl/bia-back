from django.shortcuts import render

from django.http import HttpResponse, Http404, HttpResponseRedirect

# Model
from seguridad.models import Shortener

# Create your views here.
    
def redirect_url_view(request, shortened_part):
    try:
        shortener = Shortener.objects.get(short_url=shortened_part)
        shortener.times_followed += 1        
        shortener.save()
        
        return HttpResponseRedirect(shortener.long_url)
    except:
        raise Http404('Sorry this link is broken :(')