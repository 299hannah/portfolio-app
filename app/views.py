from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm

# Create your views here.
def index(request):
    projects = Projects.objects.all()
    context={'projects':projects}
    return render(request,'portfolio.html',context)

def about(request):
    about = About.objects.first()
    ctx={'about',about}
    return render(request,'about.html',ctx)

def projects(request):
    projects = Projects.objects.filter(active=True)
    ctx = {'projects':projects}
    return render(request,'projects.html',projects)

def project(request, pk):
    project = Projects.object.get(id=pk)
    ctx={'project':project}

    return render(request,ctx,'project.html')


def profile(request):
    return render(request, 'profile.html')

# @login_required(login_urls="portfolio")
def createProject(request):
    form=ProjectForm()

    if request.method == 'Projects':
        form =ProjectForm(request.Projects,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('projects')

    ctx = {'form':form}
    return render(request, 'create.html',ctx)


