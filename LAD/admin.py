from django.contrib import admin
from .models import User

# Register your models here.
############# ADMIN CHANGES ##############
admin.site.site_header = 'eYLAD Administration'
admin.site.register(User)