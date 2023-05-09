from django.shortcuts import render

# Create your views here.
 


def filters(request):
    d={'data':'IaM gOOd PLAyer in tHE grOUNd'}



    
    return render(request,'filters.html',d)
