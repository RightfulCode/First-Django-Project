from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.show_employee, name='Read'),
    path('', views.home, name='Home'),
    path('delete/', views.delete_page, name='Delete'),
    path('deleted/<int:id>', views.delete_employee, name='Deleted'),
    path('add/', views.add_page, name='Add'),
    path('update/', views.update_page, name='Update'),
    path('updated/<int:id>', views.update_employee, name='Updated'),
]