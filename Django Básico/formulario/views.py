from django.shortcuts import render
from django.http import HttpResponse



def imc(request):
    return render(request, 'formulario.html')

def ip(request):
    altura = float(request.POST.get('altura'))
    peso = float(request.POST.get('peso'))

    imc = peso / altura * altura

    return HttpResponse(imc)

    

    

   
    


    

    
    
    


