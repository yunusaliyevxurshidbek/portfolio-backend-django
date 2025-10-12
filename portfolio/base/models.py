from django.db import models

# projects_model:
class Project(models.Model):
    project_name = models.CharField(max_length = 200)
    project_title = models.CharField(max_length = 200)
    is_published = models.BooleanField(default = False)
    project_description = models.TextField()
    project_company = models.CharField(max_length = 200)
    github_url = models.URLField(blank = True, null = True)
    project_color_type = models.CharField(max_length=100, blank = True, null = True)

    def __str__(self):
        return self.project_name
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name = "project_images", on_delete = models.CASCADE)
    image = models.FileField(upload_to = "projects/%Y/%m/%d/")
    uploaded_at = models.DateTimeField(auto_now_add = True, blank = True)

    def __str__(self):
        return f"Image for {self.project.project_name}"
    
class TechnologySection(models.Model):
    project = models.ForeignKey(Project, related_name='technology_sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='Untitled')
    details = models.TextField()


    def __str__(self):
        return f"{self.title} ({self.project.project_name})"

