from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='Home'),
    path('dept',views.dept),
    path('doctor',views.doctor),
    path('booking',views.booking),
    
]