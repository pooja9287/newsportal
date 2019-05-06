from django.db import models

class Sports(models.Model):

    title=models.CharField(max_length=80)
    img=models.ImageField(upload_to='images/')
    description=models.TextField()

class Entertainment(models.Model):

    title=models.CharField(max_length=80)
    img=models.ImageField(upload_to='images/')
    description=models.TextField()


class Politics(models.Model):

    title=models.CharField(max_length=80)
    img=models.ImageField(upload_to='images/')
    description=models.TextField()


class Editorials(models.Model):
    title=models.CharField(max_length=80)
    img=models.ImageField(upload_to='images/')
    description=models.TextField()
