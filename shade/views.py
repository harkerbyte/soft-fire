from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Members

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def members(request):
    members = Members.objects.all()
    template = loader.get_template('members.html')
    context ={
        'members':members,
    }
    return HttpResponse(template.render(context,request))


def details(request, slug):
    members = Members.objects.get(slug=slug)
    template = loader.get_template('details.html')
    context={
        'slug':members,
        }
    return HttpResponse(template.render(context, request))
'''
def testing(request):
    mymembers= Members.objects.all().values()
    user = Members.objects.filter(firstname='input_name')
    firstnames = Members.objects.values_list('firstname')
    template= loader.get_template('template.html')
    
    context={
        'firstnames':firstnames,
        'user':user,
        'members':mymembers,
        'memberlist':['Sherif','Sherifdeen','Shade']
    }
    return HttpResponse(template.render(context, request))
'''

def playgames(request):
    template=loader.get_template("games.html")
    
    return HttpResponse(template.render())

def hangman(request):
    template = loader.get_template("hangman_game.html")
    return HttpResponse(template.render())

def memory(request):
    template = loader.get_template('memory_game.html')
    return HttpResponse(template.render())