from django.contrib import admin
from .models import MoodData

class MoodDataAdmin(admin.ModelAdmin):
    list_display = ('moodtype', 'dateposted', 'user')  
    readonly_fields = ('dateposted', 'user', 'moodtype', 'token')  
    exclude = ('description',)  

admin.site.register(MoodData, MoodDataAdmin)