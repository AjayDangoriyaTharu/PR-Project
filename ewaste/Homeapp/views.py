from django.shortcuts import render,redirect,HttpResponse
from .forms import PickupForm
from .models import Pickup


from django.views.generic import View 
from rest_framework.views import APIView 
from rest_framework.response import Response 
  

# Create your views here.




def homepage(request):
    return render (request,"homepage.html")


def customer(request):
    if request.method  == 'POST':
        form =PickupForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/customer")
            except:
                pass
    else:
        form =  PickupForm()
    return render(request,'customer.html',{'form':form})        


def edit(request,id):
    pickupdata = Pickup.objects.get(id=id)
    return render(request,'edit.html',{'pickupdata':pickupdata})

def update(request,id):
    pickupdata = Pickup.objects.get(id=id)
    form = PickupForm(request.POST,instance=Pickup)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request,'edit.html',{'pickupdata':pickupdata})

def destroy(request,id):
    pickupdata = Pickup.objects.get(id=id)
    pickupdata.delete()
    return redirect('/adminpage')


def employee(request):
    return render(request,'employeepage.html')



# def report(request):
#     return HttpResponse("Report")


  
class HomeView(View): 
    def get(self, request, *args, **kwargs): 
        pickupdata = Pickup.objects.all()
        return render(request, 'admin.html',{"pickupdata":pickupdata,}) 
   
   


class ChartData(APIView): 
    authentication_classes = [] 
    permission_classes = [] 
    
    def get(self, request, format = None): 
        labels = [ 
            'Sunday', 
            'Monday',  
            'Tuesday',  
            'Wednesday',  
            'Thursday',  
            'Friday',  
            'Saturday'
            ] 
        chartLabel = "my data"
        pickupdata = Pickup.objects.all()
        chartdata = []

        for i in pickupdata:
            chartdata.append(str(i.NoItems))
        data ={ 
                     "labels":labels, 
                     "chartLabel":chartLabel, 
                     "chartdata":chartdata,
             } 
        return Response(data) 