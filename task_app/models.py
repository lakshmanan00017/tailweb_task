from django.db import models
from django.utils import timezone

class teacher(models.Model):

    username=models.CharField(max_length=100 ,null=True)
    password=models.CharField(max_length=100,null=True)



    def __str__(self):
        return self.username

class studends(models.Model):

    name=models.CharField(max_length=100 ,null=True)
    subject=models.CharField(max_length=100,null=True)
    mark=models.IntegerField(default=0)

    def __str__(self):
        return self.name
    


class AuditLog(models.Model):
    teacher_id = models.IntegerField()
    student_id = models.IntegerField()
    new_marks = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)