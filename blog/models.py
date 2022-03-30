from django.db import models

class Blog(models.Model):    # БД django Blog связываем с нашей Model
    title= models.CharField(max_length=200)         # в заголовках нашей страницы будет не более 200 символов
    description= models.TextField()   
    date=models.DateField()  

def __str__(self):
    return self.title