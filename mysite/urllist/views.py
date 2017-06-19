from . import PlotHtmlMaker
from django.http import HttpResponse
from django.template import loader
import datetime
import codecs

def index(request):
    #return render(request, '/post_list.html', {})
    #return HttpResponse("Hello, world. You're at the polls index.2")
    #now = datetime.datetime.now()
    PlotHtmlMaker.makeit()
    htmlFile = codecs.open("urllistgraph.html", 'r')
    html =  htmlFile.read()
    # html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


