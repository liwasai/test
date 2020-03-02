from django.db import models

# Create your models here.
class news(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey("user",on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    con = models.TextField()


class user(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    head = models.ImageField(upload_to="img")


class comment(models.Model):
    c_user = models.ForeignKey("user",on_delete=models.CASCADE)
    c_news = models.ForeignKey("news",on_delete=models.CASCADE)
    write = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    good_num = models.PositiveIntegerField()


class reply(models.Model):
    r_com = models.ForeignKey("comment",on_delete=models.CASCADE)
    r_user = models.ForeignKey("user",on_delete=models.CASCADE)
    write_con = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    good_num = models.PositiveIntegerField()




