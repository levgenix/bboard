# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Bb


def index(request):
    #bbs = Bb.objects.order_by('-published')
    #template = loader.get_template('bboard/index.html')
    #context = {'bbs': bbs}
    #return HttpResponse(template.render(context, request))
    return render(request, 'bboard/index.html', {'bbs': Bb.objects.all()})
