from django.db import models


class CourseModel(models.Model):
    cid = models.AutoField(primary_key = True)
    cname = models.CharField(max_length=50)
    cfaculty = models.CharField(max_length=100)
    cdate = models.DateField(auto_now=False)
    ctime = models.TimeField(auto_now_add=False)
    cfee = models.FloatField()
    cduration = models.CharField(max_length=50)


class StudentModel(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    contact_no = models.IntegerField(unique=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    scourses = models.ManyToManyField(CourseModel)









