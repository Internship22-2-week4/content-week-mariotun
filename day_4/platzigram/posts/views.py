#from django.shortcuts import render
# Create your views here.

from django.shortcuts import render
#from django.http import HttpResponse
from datetime import datetime


datos = [
    {
        'title':'Mont blanc',
        'user':{
            'name':'Yesica Cortes',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600/?image=1036',
    },
    {
        'title':'Via lactea',
        'user':{
            'name':'C. Vander',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'title':'Nuevo auditorio',
        'user':{
            'name':'Thespianartist',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200/?image=1076',
    }
]


def list_posts(request):
    return render(request,'feed.html',{'posts':datos})
    '''content = []
    for post in datos:
        content.append("""
        <p><strong>{name}</strong></p>
        <p><small>{user} - <i>{timestamp}</i></small></p>
        <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))'''