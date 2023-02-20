from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ApplicationForm
from .models import Application

# Create your views here.

def index(request):
    return render(request, 'index.html')

def show_applications(_request):
    applications = list(Application.objects.values())
    application_data = {'applications': applications}
    return JsonResponse(application_data)

def show_job_info(request, id_application):
    application = get_object_or_404(Application, pk=id_application)
    job_info = application.job_description
    return render(request, 'job_info.html', {'job_info': job_info})
    
def show_comment(request, id_application):
    application = get_object_or_404(Application, pk=id_application)
    comment = application.commentary
    return render(request, 'comment.html', {'comment': comment})


def add_application(request):
    if request.method == 'POST':
        new_application = ApplicationForm(request.POST)
        if new_application.is_valid():
            new_application.save()
            return redirect('index')
    else:
        application_form = ApplicationForm
        return render(request, 'add.html', {'application_form': application_form})

def edit_application(request, id_application):
    application = get_object_or_404(Application, pk=id_application)

    if request.method == 'POST':
        edited_application = ApplicationForm(request.POST, instance=application)
        if edited_application.is_valid():
            edited_application.save()
            return redirect('index')
    else:
        app_form = ApplicationForm(instance=application)
        return render(request, 'edit.html', {'app_form': app_form})


def delete_application(request, id_application):
    if request.method == 'POST':
        return redirect('confirm_delete', id_application=id_application)
    else:
        return render(request, 'delete.html', {'id_application': id_application})

def confirm_delete(request, id_application):
    application = get_object_or_404(Application, pk=id_application)
    application.delete()
    return redirect('index')
