from django.shortcuts import render

def home(request):
    return render(request,'index2.html',{})

def message(request):
    return render(request,'message2.html',{})

def offlinemap(request):
    return render(request,'map.html',{})    
