from django.shortcuts import render
from .forms import PredictionForm

# Create your views here.
def home(request):
    return render(request, "base/home.html")

# Create your views here.
def predict(request):
    form = PredictionForm()
    return render(request, "base/predict.html", {"form":form})

# Create your views here.
def analysis(request):
    return render(request, "base/analysis.html")
