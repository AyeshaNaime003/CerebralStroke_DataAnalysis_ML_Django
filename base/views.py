from django.shortcuts import render
from django.conf import settings
from .models import Prediction
from django.contrib import messages
import os
import joblib
import numpy as np
import pandas as pd

base_dir = settings.BASE_DIR

# Create your views here.
def home(request):
    return render(request, "base/home.html")

# Create your views here.
def predict(request):
    result = None
    if request.method=="POST":
        # get data from post request
        gender = 1 if request.POST.get('gender')=="male" else 0
        age = int(request.POST.get('age'))
        weight = float(request.POST.get('weight'))
        height = float(request.POST.get('height'))
        smoking_statuses = {'never':0, 'formerly':1, 'smokes':2}
        smoking_status = smoking_statuses[request.POST.get('smoking_status')]
        ever_married = 1 if request.POST.get('ever_married') == "yes" else 0
        work_type_mapping = {
            'govt_job': 0,
            'never_worked': 1,
            'private': 2,
            'self-employed': 3,
            'children': 4,
        }
        work_type = work_type_mapping.get(request.POST.get('work_type'), None)
        residence_type = 1 if request.POST.get('Residence_type') == "urban" else 0
        heartdisease = 1 if request.POST.get('heart-disease') == "yes" else 0
        hypertension = 1 if request.POST.get('hypertension') == "yes" else 0
        avg_glucose_lvl = float(request.POST.get('avg-glucose-lvl'))
        bmi = weight/height**2
        # standardizing
        loaded_scaler = joblib.load(os.path.join(base_dir,"base","scaler_model.joblib"))
        mean_values = loaded_scaler.mean_
        std_values = loaded_scaler.scale_
        s_age = (age - mean_values[0]) / std_values[0]
        s_avg_glucose_lvl = (avg_glucose_lvl - mean_values[1]) / std_values[1]
        s_bmi = (bmi - mean_values[2]) / std_values[2]

        # create the model input
        work_type_array = np.zeros((5))
        work_type_array[work_type]=1
        data_array = [gender,
                      s_age,
                      hypertension,
                      heartdisease,
                      ever_married,
                      residence_type,
                      s_avg_glucose_lvl,
                      s_bmi,
                      smoking_status]+list(work_type_array)
        
        rf_smote = joblib.load(os.path.join(base_dir,"base","rf_smote.joblib"))
        result = rf_smote.predict([data_array])[0]
        # create prediction obeject
        prediction = Prediction(
            gender=request.POST.get('gender'),
            age=request.POST.get('age'),
            bmi=bmi,
            work_type=request.POST.get('work_type'),
            smoking_status=request.POST.get('smoking_status'),
            avg_glucose_lvl=request.POST.get('avg-glucose-lvl'),
            heartdisease=request.POST.get('heartdisease'),
            hypertension=request.POST.get('hypertension'),
            risk=result
        )
        prediction.save()
        messages.success(request, 'Prediction saved successfully!')

    return render(request, "base/predict.html", {"result":result})

# Create your views here.
def analysis(request):
    return render(request, "base/analysis.html")
