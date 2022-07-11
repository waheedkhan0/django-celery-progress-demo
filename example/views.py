from django.shortcuts import render
from time import sleep

from .tasks import go_to_sleep

# Create your views here.
def index(request):
    task = go_to_sleep.delay(1)
    return render(request,'example/index.html',context={'task_id': task.task_id})