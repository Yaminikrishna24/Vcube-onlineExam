from django.contrib import admin
from .models import userdetails,Course,Batch,Gender

# Register your models here.
admin.site.register(Gender)
admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(userdetails)