from django.contrib import admin
from .models import User, Article, Author
# Register your models here.
CustomUser = User
admin.site.register(CustomUser)


# Register your models here.
#Maakt het mogelijk om bij het admin paneel deze dingen te wijzigen.
admin.site.register(Article)
admin.site.register(Author)
