from django.db import models    # база данных django

class project(models.Model):    # БД django model связываем с нашей Model
    title= models.CharField(max_length=100)         # в заголовках нашейстраницы будет не более 100 символов
    description= models.CharField(max_length=250)   # в описаниях не более 250-
    image=models.ImageField(upload_to='portfolio/images')  
    url= models.URLField(blank=True)
# дописываем для отображения названия поста
def __str__(self):
    return self.title