from django.db import models

class Article(models.Model):
    article=models.CharField(max_length=20)
    counter=models.IntegerField()

    
    