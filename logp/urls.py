from django.urls import path
from .import views
urlpatterns=[
    path('Home',views.index,name='Home'),
    path('login/',views.signin,name='signin'),
    path('register/',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('viewall/',views.viewall,name='viewall'),
    path('updatereg/<str:pk>/',views.updatereg,name='updatereg'),
    path('updatereg/updatedata/<str:pk>',views.updatedata,name='updaterecord'),
    path('deletereg/<str:pk>/',views.deletereg,name='deletereg'),
]