from django.contrib import admin
from .models import LADUser, Theme, DiscourseAPI

# Register your models here.
############# ADMIN CHANGES ##############
admin.site.site_header = 'eYLAD Administration'
admin.site.register(LADUser)
admin.site.register(Theme)
# admin.site.register(DiscourseAPI)


class AdminDiscourseAPI(admin.ModelAdmin):
    model = DiscourseAPI
    list_display = ('name', 'url')

admin.site.register(DiscourseAPI, AdminDiscourseAPI)
