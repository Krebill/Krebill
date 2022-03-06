from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.

def home(request):
    projets = Project.objects.all()
    detailskills = skill.objects.exclude(body='')
    skills = skill.objects.filter(body='')
    endoces = Endocement.objects.filter(approuvé=True)
    
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre message a été envoyer.')        
    
    context = {
        'endoces':endoces,
        'form':form,
        'projets':projets,
        'skills':skills,
        'detailskills':detailskills
    }
    return render(request,'base/home.html', context)

def projetpage(request, pk):
    projets = Project.objects.get(id=pk)
    # nombre  de commentaire
    count = projets.comment_set.count()
    # Les personnes et leurs commentaire
    comments = projets.comment_set.all().order_by('-created')
    
    # validation du commentaire
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.projet = projets
            comment.save()    
    context = {
        'projets':projets,
        'form':form,
        'count':count,
        'comments':comments
     }
    return render(request, 'base/projet.html', context)

def ajoutprojet(request):
    forms = Projetform()
    if request.method == 'POST':
        forms = Projetform(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('home')
        
    context = {'forms':forms}
    return render(request, 'base/projet_form.html', context)


def modifier(request, pk):
    projets = Project.objects.get(id=pk)
    forms = Projetform(instance=projets)
    if request.method == 'POST':
        forms = Projetform(request.POST, request.FILES, instance=projets)
        if forms.is_valid():
            forms.save()
            return redirect('home')
        
    context = {'forms':forms}
    return render(request, 'base/projet_form.html', context)

def inbox(request):
    inbox = Message.objects.all().order_by('is_read')
    nonlu = Message.objects.filter(is_read=False).count()
    context = {
        'inbox':inbox,
        'nonlu':nonlu,
    }
    return render(request,'base/inbox.html', context)

def messagepage(request,pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    context = {
        'message':message,
    }
    return render(request,'base/message.html', context)


def ajoutskill(request):
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        form.save()
        return redirect('home')    
    context = {
        'form':form,
    }
    return render(request, 'base/skill_form.html', context )


def ajoutendo(request):
    form = EndoForm()
    if request.method == 'POST':
        form = EndoForm(request.POST)
        form.save()
        return redirect('home')    
    context = {
        'form':form,
    }
    return render(request, 'base/endo_form.html', context )

def pourboire(request):
    return render(request, 'base/donation.html')

def chartpage(request):
    
    return render(request, 'base/charts.html')