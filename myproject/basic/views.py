from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def sample(request):
    qp1=request.GET.get("name")
    qp2=request.GET.get("city")
    return HttpResponse(f"{qp1} is from {qp2}")

def sample1(request):
    info={"data":[{"name":"subbu","age":"21","city":"hyd","gender":"male"},{"name":"pavan","age":"23","city":"prakasam","gender":"male"},{"name":"siri","age":"21","city":"hyd","gender":"female"},{"name":"gopi","age":"23","city":"karnool","gender":"male"},{"name":"Krishna","age":"21","city":"guntur","gender":"male"}]}
    return JsonResponse(info)

