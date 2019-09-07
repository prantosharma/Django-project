from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Contact
# Register your models here.

class ConntactAdmin(admin.ModelAdmin):
    list_display=('id','Name','email','phone','information','gender')
    list_editable=('information',)
    list_per_page= 5
    search_fields=('Name','email','phone','information','gender')
    list_filter=('gender','date_added')

    

admin.site.register(Contact,ConntactAdmin)
admin.site.unregister(Group)