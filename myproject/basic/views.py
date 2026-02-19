from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import math
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


def productInfo(request):
    product_name=request.GET.get("name","mobile")
    quantity=int(request.GET.get("quantity",3))
    price_=int(request.GET.get("price",25000))
    total=request.GET.get(price_*quantity)
    data={"productname":product_name,"quantity":quantity,"price":price_,"total_":quantity*price_}
    return JsonResponse(data)


def fitlerStudentsBycity(request):
    student_data=[{'name':'subbu','city':'hyd'},{'name':'pavan','city':'bng'},{'name':'sai','city':'hyd'},{'name':'krish','city':'bgn'},{'name':'ram','city':'hyd'},{'name':'lakshman','city':'bgn'}]
    filterStudents=[]
    city=request.GET.get("city","hyd")

    for student in student_data:
       if student["city"]==city:
           filterStudents.append(student)
    return JsonResponse({"status":"success","data":filterStudents})



def filterData(request):
    data=[1,2,3,4,5,6,7,8,9,10]
    filterData=[]
    qp=int(request.GET.get("num",2))
    for x in data:
        if x%qp==0:
            filterData.append(x)
    return JsonResponse({"data":filterData})

def pagination(request):
    data=['banana','apple','carrot','graps','watermelon','kiwi','pineapple','custard-apple','strawberry','blueberry','dragonfruit']
    page=int(request.GET.get("page",1))
    limit=int(request.GET.get("limit",3))

    start=(page-1)*limit
    end=page*limit

    total_page=math.ceil(len(data)/limit)
    result=data[start:end]
    res={"status":"success","page":page,"total_page_":total_page,"data":result}
    return JsonResponse(res)


