from os import path
from django.shortcuts import render, get_object_or_404, redirect #, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse 
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from asgiref.sync import async_to_sync

from .entities import Hosts
from .forms import PlaybookForm
from .models import Playbook

@login_required
def index(request):
    playbooks = Playbook.objects.all()
    #playbooks = get_list_or_404(Playbook)
    return render(request,'ansible_web/index.html',{'playbooks':playbooks})

@login_required
def hosts(request):
    hosts = Hosts(settings.MEDIA_ROOT+"/hosts")
    return render(request, 'ansible_web/hosts.html',{'hosts': hosts.get_hosts().items()})

@login_required
def get_playbook(request, pk):
    #playbook = Playbook.objects.get(pk=pk)
    playbook = get_object_or_404(Playbook, pk=pk)
    file_name = settings.MEDIA_ROOT+str(playbook.script)
    if path.exists(file_name):
        with open(file_name,'r') as f:
            response = HttpResponse(content_type='text/yaml')
            response['Content-Disposition'] = f'attachment; filename="{playbook.script}"'
            response.write(f.read())
            return response
    else:
        return Http404(f"{file_name}<br/> is not exist!")

@login_required
def delete_playbook(request, pk):
    Playbook.objects.get(pk=pk).delete()
    return redirect('/home/')

class PlaybookCreate(CreateView):
    model = Playbook
    #fields = ['name', 'details', 'script']
    form_class = PlaybookForm

class PlaybookUpdate(UpdateView):
    model = Playbook
    #fields = ['name', 'details', 'script']
    form_class = PlaybookForm

class PlaybookDelete(DeleteView):
    model = Playbook
    success_url = reverse_lazy('ansible_web:index')


'''
    if request.POST:
        client = Client.objects.first()
        form = PlaybookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return reverse_lazy('home')
    else:
        form = PlaybookForm()
    return render(request, 'ansible_web/name.html', {'form': form})
'''