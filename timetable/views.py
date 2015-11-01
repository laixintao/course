# Create your views here.

from django.shortcuts import render_to_response,render,get_object_or_404
from django.template.context import RequestContext
from forms import courseForm

def publish(request):
    if request.method == 'GET':
        form = courseForm()
        return render_to_response('publish.html',RequestContext(
            request,
            {'form':form,}
        ))
    else:
        form = courseForm(request.POST)
        if form.is_valid():
            pass
        else:
            pass
        return render_to_response('publish.html',RequestContext(request,{'form':form,}))