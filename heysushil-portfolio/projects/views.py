from django.shortcuts import render
from projects.models import Projects

# Create your views here.
def project_index(request):
    projects = Projects.objects.all()
    context = {'projects':projects}
    return render(request, 'projects_index.html', context)

def project_detial(request, pk):
    project = Projects.objects.get(pk=pk)
    context = {'data':project}
    return render(request, 'project_detail.html', context)