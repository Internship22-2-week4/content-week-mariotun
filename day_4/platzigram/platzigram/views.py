from django.http import HttpResponse 
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('HOLA MUNDO, CURRENT SERVER TIME IS {now}'.format(now=now))


def sort_integers(request):
    #print(request)
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status':'ok',
        'numbers': sorted_ints,
        'message':'Integers sorted successfully'
    }

    #import pdb; pdb.set_trace() # [int(i) for i in numbers.split(',')]
    return HttpResponse(json.dumps(data),content_type='application/json')

def say_hi(request,name,age):
    if age < 12 :
        message = 'Sorry {} , you are not allowed here'.format(name)
    else:
        message = 'Hello {}! , welcome to Platzigram'.format(name)
    
    return HttpResponse(message)
