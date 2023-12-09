from django.db import models
from django.contrib.auth.models import User

class Prediction(models.Model):
    # Foreign Key relationship with the User model
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='predictions')

    # Fields for predictions
    GENDER_CHOICES = [ ('male', 'Male'),
        ('female', 'Female'),]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    age = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()

    SMOKING_STATUS_CHOICES = [  ('never', 'Never Smoked'),
        ('formerly', 'Formerly Smoked'),
        ('smokes', 'Currently Smokes'),]
    smoking_status = models.CharField(max_length=10, choices=SMOKING_STATUS_CHOICES)

    RISK_CHOICES = [ (0, 'Low Risk'),
        (1, 'High Risk'),]
    risk = models.IntegerField(choices=RISK_CHOICES)


    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Prediction for {self.user.username}'

    class Meta:
        ordering = ['-created']  # Order by creation time (latest first)

