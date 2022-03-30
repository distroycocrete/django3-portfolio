from django.contrib import admin

# импорт моделей из текущей паки с классом Project
from portfolio.models import project

admin.site.register(project)
