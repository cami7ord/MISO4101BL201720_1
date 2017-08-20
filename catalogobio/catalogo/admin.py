from django.contrib import admin

# Register your models here.
from .models import UserProfile
from .models import Category
from .models import Species



class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_username', 'country', 'city')

    def user_username(self, instance):
        return instance.user.username

class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name', 'category', 'description')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Species, SpeciesAdmin)
admin.site.register(Category)
