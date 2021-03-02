from django.shortcuts import render
import joblib
def index(request):
    return render(request,'iris_model/home.html')

def result(request):
    cls=joblib.load("finalized_model.sav")
    li=[]
    li.append(request.GET['sepal-length'])
    li.append(request.GET['sepal-width'])
    li.append(request.GET['petal-length'])
    li.append(request.GET['petal-width'])
    ans=cls.predict([li])
   

    return render(request,'iris_model/result.html',{'ans':ans})