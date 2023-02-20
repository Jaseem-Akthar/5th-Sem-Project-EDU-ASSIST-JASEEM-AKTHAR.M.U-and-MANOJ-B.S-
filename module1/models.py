from django.db import models


class usercrd(models.Model):
    email=models.CharField(max_length=25,primary_key=True)
    pswd=models.CharField(max_length=25)
    confirmpassword=models.CharField(max_length=25)

class imagedata(models.Model):
    iname=models.CharField(max_length=30)
    imagePath=models.ImageField(upload_to='notes/')

class usercontact(models.Model):
    name=models.CharField(max_length=30,primary_key=True)
    email=models.CharField(max_length=25)
    number=models.CharField(max_length=30)
    course=models.CharField(max_length=25)
    # gender=models.CharField(maxlength=4)
