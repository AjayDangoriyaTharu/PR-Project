from django.urls import path
from Homeapp import views


urlpatterns = [

    #dashboard

    path('', views.homepage, name='homepage'),
    path('employee/', views.employee, name='employee'),
    path('customer', views.customer,name='customer'),
    # path('adminpage', views.adminpage,name='adminpage'),

    #Admin_Chart.js
    path('adminpage', views.HomeView.as_view(),name="adminpage"), 
    path('api', views.ChartData.as_view()), 

    #pickup
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),



]
