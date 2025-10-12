from django.contrib import admin
from .models import Project, TechnologySection, ProjectImage

class TechnologySectionInline(admin.TabularInline):
    model = TechnologySection
    extra = 1

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("project_name", "project_title", "is_published", "project_company")
    search_fields = ("project_name", "project_title", "project_company")
    list_filter = ("is_published",)
    inlines = [TechnologySectionInline, ProjectImageInline]

admin.site.register(TechnologySection)
admin.site.register(ProjectImage)
