from django.urls import re_path, include
from . import views

urlpatterns=[
    re_path(r'^index$', views.index, name='index'),
    re_path(r'^Devapplyleav$', views.Devapplyleav, name='assigned'),
    re_path(r'^Devapplyleav1$', views.Devapplyleav1, name='dashboard'),
    re_path(r'^Devapplyleav2$', views.Devapplyleav2, name='project'),
    re_path(r'^Devleaverequiest$', views.Devleaverequiest, name='projectdetails'),
    re_path(r'^Devattendance$', views.Devattendance, name='submitted'),
    re_path(r'^Devapplyleav3$', views.Devapplyleav3, name='task'),
    re_path(r'^Tattend$', views.Tattend, name='task'),
    re_path(r'^Manager_index$', views.Manager_index, name='Manager_index'),
    re_path(r'^Manager_accepted_projects$', views.Manager_accepted_projects, name='Manager_accepted_projects'),
    re_path(r'^Manager_rejected_projects$', views.Manager_rejected_projects, name='Manager_rejected_projects'),
]