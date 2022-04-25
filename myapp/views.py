from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import paraphrase


# Create your views here.
def hello(request):
    #text = "<h1>welcome to my app number %s!</h1>"%number
    #return HttpResponse(text)
    today= datetime.now().date()
    
    return render(request,'myapp/templates/index.html',{"today" : today})

def form(request):
    data=request.POST.get('num')
    if data:
        result =paraphrase(data)
    else:
        result = "Some random sentences..."
    
    return render(request,"myapp/templates/form.html",{"result" : result})

#def form(request):
   
#   result = paraphrase(num)
#   return render(request,"myapp/templates/form.html",{"result":result, 'num':num}) 
    

"""
from django.shortcuts import render

def hello(request):
    return render(request,"myapp/templates/hello.html",{})
"""
def viewArticle(request,username='Simple User'):
    text = "<h1>Displaying article Number :{}</h1>".format(username)
    return HttpResponse(text)