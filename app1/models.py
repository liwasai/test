from django.db import models

# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=10,unique=True)
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=6)
    pic = models.ImageField(upload_to="img_user")


class comment(models.Model):
    con = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    c_user = models.ForeignKey("user",on_delete=models.CASCADE)
    c_ess = models.ForeignKey("essay",on_delete=models.CASCADE)


class essay(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()







