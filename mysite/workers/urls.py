from django.urls import path
from .views import *

urlpatterns = [path('', index, name="home"),
               path('list_workers/', WorkersView.as_view(), name='list_workers'),
               path('employee_month/', employee_month, name="employee_month"),
               path('add_worker/', AddWorker.as_view(), name="add_worker")]