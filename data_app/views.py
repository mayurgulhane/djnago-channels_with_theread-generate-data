from django.shortcuts import render
from django.http import JsonResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
import time
from .thread import *


# Create your views here.


def test(request):
    for i in range(1,10):
        channel_layer = get_channel_layer()
        data = {'count':i}
        (channel_layer.group_send)(
          'test_consumer_group',{
              'type':'send_notification',
              'value':json.dumps(data)
          }
        )
        time.sleep(1)
    return render(request, 'home.html')



async def home(request):

    return render(request, 'home.html')


def genrate_student_data(request):
    total = request.GET.get('total')
    CreateStudentThread(int(total)).start()

    return JsonResponse({'status':200})