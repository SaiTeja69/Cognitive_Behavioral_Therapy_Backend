from django.shortcuts import render,get_object_or_404


def home(request):
    return render(request,'index.html')

def info(request):
	return render(request,'info.html')