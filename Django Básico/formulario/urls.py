from django.urls import path
from . import views

urlpatterns = [ 
    path('imc/', views.imc, name="resultado"),
    path('ip/', views.ip, name='ip')

    
]