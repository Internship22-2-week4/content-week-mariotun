from django.http import HttpResponse 
from datetime import datetime

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('HOLA MUNDO, CURRENT SERVER TIME IS {now}'.format(now=now))


def miName(request):
    #print(request)
    import pdb; pdb.set_trace()
    return HttpResponse('My name is Mario')