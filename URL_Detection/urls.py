# urls.py
from django.contrib import admin
from django.urls import path
#from .views import home, result  # Import home function from views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    #path('', views.home, name = "home"),  # Map the root URL to the home function
    #path('result/',views.result, name ="result")
]