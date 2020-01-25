from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
number=[1,2,3,4,5,6,7,8]
sem1=['Engineering Mathematics-1','Engineering Physics-1']
sem2=['Engineering Mathematics-2','Engineering Physics-2']
sem3=['Engineering Mathematics-3','Engineering Physics-3']
sem4=['Engineering Mathematics-4','Engineering Physics-4']
sem5=['Engineering Mathematics-5','Engineering Physics-5']
sem6=['Engineering Mathematics-6','Engineering Physics-6']
sem7=['Engineering Mathematics-7','Engineering Physics-7']
sem8=['Engineering Mathematics-8','Engineering Physics-8']
def home(request):
    return render(request,"index.html ",{'number':number})
def semester(request):
    return render(request,"SEM.html",{'number':number,'sem1':sem1,'sem2':sem2,'sem3':sem3,'sem4':sem4,'sem5':sem5,'sem6':sem6,'sem7':sem7,'sem8':sem8})
