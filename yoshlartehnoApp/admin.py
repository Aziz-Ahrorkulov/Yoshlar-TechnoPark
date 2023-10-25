from django.contrib import admin
from .models import Project, Video
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', )

admin.site.register(Project, ProjectAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )

admin.site.register(Video, VideoAdmin)