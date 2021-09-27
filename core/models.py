from django.db import models

class Person(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    supervisor_name = models.CharField(max_length=100)
    system_number = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    