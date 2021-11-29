from django.contrib import admin
from .models import Students
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('usn','fname', 'lname','ten_ma','tw_ma',)

admin.site.register(Students,StudentAdmin)
