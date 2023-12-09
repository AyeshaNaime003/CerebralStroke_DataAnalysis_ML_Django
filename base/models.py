from django.db import models
from django.contrib.auth.models import User

class Prediction(models.Model):    
    # Fields for predictions
    # gender
    GENDER_CHOICES = [ ('male', 'Male'),
        ('female', 'Female'),]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    # age
    age = models.IntegerField()
    # bmi
    bmi = models.FloatField()
    # work
    WORK_TYPE_CHOICES = [
        ('govt_job', 'Government Job'),
        ('never_worked', 'Never Worked'),
        ('private', 'Private Job'),
        ('self-employed', 'Self-Employed'),
        ('children', 'Children'),
    ]
    work_type = models.CharField(max_length=15, choices=WORK_TYPE_CHOICES, default="govt_job")
    # smoking
    SMOKING_STATUS_CHOICES = [  ('never', 'Never Smoked'),
        ('formerly', 'Formerly Smoked'),
        ('smokes', 'Currently Smokes'),]
    smoking_status = models.CharField(max_length=10, choices=SMOKING_STATUS_CHOICES)
    # average glucose level
    avg_glucose_lvl = models.FloatField()
    # heart disease
    HEART_DISEASE_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    heartdisease = models.CharField(max_length=3, 
    choices=HEART_DISEASE_CHOICES, default="no", null=True)
    # hypertensions
    HYPERTENSION_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    hypertension = models.CharField(max_length=3, choices=HYPERTENSION_CHOICES, default="no")
    # risk
    RISK_CHOICES = [ (0, 'Low Risk'),
        (1, 'High Risk'),]
    risk = models.IntegerField(choices=RISK_CHOICES)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']  # Order by creation time (latest first)

