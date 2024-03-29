from django.shortcuts import render
from django.http import HttpResponse, FileResponse, Http404
from django.template import loader

# Create your views here.
from django.http import HttpResponse


def index(request):
    #template = loader.get_template('about.html')
    #return HttpResponse(template.render())
    return render(request, 'home.html')

def detail(request):
    #template = loader.get_template('about.html')
    #return HttpResponse(template.render())
    return render(request, 'about.html')

def contact(request):
    #template = loader.get_template('about.html')
    #return HttpResponse(template.render())
    return render(request, 'contact.html')

def resume(request):
    return resumeDirect(request)

def resumeDirect(request):
    return FileResponse(open('static/AboutContact/Resume.pdf', 'rb'))

def researchPaper(request):
    return researchPaperDirect(request)

def researchPaperDirect(request):
    return FileResponse(open('static/AboutContact/ResearchPaper.pdf', 'rb'))

def webScraper(request):
    return webScraperDirect(request)

def webScraperDirect(request):
    return FileResponse(open('static/AboutContact/WebScrapeReport.pdf', 'rb'))

def pong(request):
    return render(request, 'pong.html')

def snek(request):
    return render(request, 'snek.html')

def solar(request):
    return render(request, 'solar.html')