from django.db import models

# Create your models here.
from django.db import models
from authentication.models import User

class StudentProgress(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.TextField()
    date = models.DateField()
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="progress_updates")
