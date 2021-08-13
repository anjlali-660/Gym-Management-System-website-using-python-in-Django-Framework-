from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('About/',views.About),
    path('Services/',views.Services),
    path('Contact/',views.Contact),
    path('login/',views.admin_login),
    path('admin_homepage/',views.admin_homepage),
    path('logout/',views.admin_logout),
    path('add_enquiry/',views.add_enquiry),
    path('view_enquiry/',views.view_enquiry),
    path('add_equipments/',views.add_equipments),
    path('view_equipments/',views.view_equipments),
    path('add_plan/',views.add_plan),
    path('view_plan/',views.view_plan),
    path('delete_enquiry/',views.delete_enquiry),
    path('delete_equipments/',views.delete_equipments),
    path('delete_plan/',views.delete_plan),
    path('add_member/',views.add_member),
    path('view_member/',views.view_member),
        path('delete_member/',views.delete_member),


]
