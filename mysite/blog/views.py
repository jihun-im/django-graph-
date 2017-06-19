from django.shortcuts import render
from django.http import HttpResponse
import datetime



def post_list(request):
    #return render(request, '/post_list.html', {})    
    #return HttpResponse("Hello, world. You're at the polls index.2")
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

