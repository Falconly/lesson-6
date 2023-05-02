from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Worker
from .forms import AddWorkerForm
from .services import get_worker


# Create your views here.

def index(request):
    return render(request, 'workers/base.html', context={'title': 'Информация о сотрудниках'})


class WorkersView(ListView):
    model = Worker
    context_object_name = 'workers'
    template_name = "workers/list_workers.html"
    ordering = ('-id',)
    extra_context = {'title': 'Список сотрудников'}


def employee_month(request):
    worker = get_worker(request)

    context = {'title': 'Сотрудник месяца',
               'worker': worker}
    return render(request, 'workers/employee_month.html', context=context)


class AddWorker(CreateView):
    form_class = AddWorkerForm
    template_name = 'workers/add_worker.html'
    extra_context = {'title': 'Добавление сотрудника'}
