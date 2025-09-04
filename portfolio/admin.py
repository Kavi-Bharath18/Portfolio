from django.contrib import admin
from .models import Skill, Project
from .models import Images, Resume

admin.site.register(Resume)
admin.site.register(Images)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'tags', 'summary', 'description')
    list_filter = ('created_at',)


