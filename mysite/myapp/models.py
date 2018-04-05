from django.db import models

class Donor(models.Model):
    name=models.CharField(max_length=264)
    blood_group=models.CharField(max_length=264)
    dob=models.DateField()
    gender=models.CharField(max_length=1)
    phone=models.CharField(max_length=264)
    email_id=models.CharField(max_length=264)
    medicalHistory=models.TextField()
    location=models.CharField(max_length=200,default='Delhi')
    a1=models.IntegerField(null=True,blank=True)
    a2=models.IntegerField(null=True,blank=True)
    a3=models.IntegerField(null=True,blank=True)
    a4=models.IntegerField(null=True,blank=True)
    a5=models.IntegerField(null=True,blank=True)
    a6=models.IntegerField(null=True,blank=True)

class Acceptor(models.Model):
    name=models.CharField(max_length=264)
    blood_group=models.CharField(max_length=264)
    dob=models.DateField()
    gender=models.CharField(max_length=1)
    phone=models.CharField(max_length=264)
    email_id=models.EmailField(max_length=264)
    medicalHistory=models.TextField()
    location=models.CharField(max_length=200,default='Delhi')
    a1=models.IntegerField(null=True,blank=True)
    a2=models.IntegerField(null=True,blank=True)
    a3=models.IntegerField(null=True,blank=True)
    a4=models.IntegerField(null=True,blank=True)
    a5=models.IntegerField(null=True,blank=True)
    a6=models.IntegerField(null=True,blank=True)


class Help(models.Model):
    name = models.CharField(max_length=264)

    def __str__(self):
        return self.name
