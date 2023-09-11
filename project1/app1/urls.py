
from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.home,name='home'),
    path('regadmin/',views.regadmin,name='regadmin'),
    path('loginadmin/',views.loginadmin,name='loginadmin'),
    path('loginadmin/',views.loginadmin,name='loginadmin'),
    path('admindashboard/',views.admindashboard,name='admindashboard'),

    #-----------------------------------------------------------------
    path('reguser/',views.reguser,name='reguser'),
    path('loginuser/',views.loginuser,name='loginuser'),
    path('userdashboard/',views.userdashboard,name='userdashboard'),
    #----------------------------------------------------------------
    path('query/',views.query,name='query'),
    path('insertquery/',views.insertquery,name='insertquery'),
    #------------------------------------------------------------
    path('showquery/',views.showquery,name='showquery'),
    path('update/<int:id>',views.update,name='update'),
    path('showupdate/<int:id>',views.showupdate,name='showupdate'),
    path('delete/<int:id>',views.delete,name='delete'),

]

