from django.db import models

# Create your models here.

class FaceModel(models.Model):

    pic = models.FileField(upload_to='files')
