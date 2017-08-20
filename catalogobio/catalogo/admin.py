from django.contrib import admin

# Register your models here.
from .models import UserProfile
from .models import Category
from .models import Species

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Species)
