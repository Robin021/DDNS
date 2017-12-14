from django.shortcuts import render

# Create your views here.
def ip(request):
    context		= {}
    context['hello']	= 'Welcome' 
    return render(request,'ip.html',context)
