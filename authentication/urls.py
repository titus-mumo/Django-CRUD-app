from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'),#get and post request for insert operation
    path('<int:id>/', views.employee_form, name='employee_update'),#get and post request for update operation
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
    path('list/', views.employee_list),#get and post request to retrieve and display all records
]