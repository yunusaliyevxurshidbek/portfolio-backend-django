from rest_framework import serializers
from base.models import Project, ProjectImage, TechnologySection
from base.models import Project, TechnologySection, ProjectImage


class TechnologySectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologySection
        fields = ["title", "details"]

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ["image"]

class ProjectSerializer(serializers.ModelSerializer):
    technology_sections = TechnologySectionSerializer(many = True, read_only = True)
    project_images = ProjectImageSerializer(many = True, read_only = True) 

    class Meta:
        model = Project
        fields = "__all__"