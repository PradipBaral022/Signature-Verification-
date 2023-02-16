from django.db import models

class login(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    