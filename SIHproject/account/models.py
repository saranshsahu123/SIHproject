from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100, default='Anonymous')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=[('learner', 'Learner'), ('admin', 'Admin')])

    def __str__(self):
        return self.name
