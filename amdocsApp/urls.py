from django.urls import path,include
from amdocsApp import views
urlpatterns = [
    path("",views.index,name='amdocsApp'),	
    path("contact",views.contact,name='contact')
	]
