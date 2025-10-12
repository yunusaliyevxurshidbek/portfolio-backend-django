from rest_framework import serializers
from base.models import Project, ProjectImage, TechnologySection
from base.models import Project, TechnologySection, ProjectImage
from django.conf import settings


class TechnologySectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologySection
        fields = ["title", "details"]

class ProjectImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = ProjectImage
        fields = ["image_url"]

    def get_image_url(self, obj):
        if obj.image and hasattr(obj.image, "url"):
            base_url = settings.AWS_S3_ENDPOINT_URL
            bucket_name = settings.AWS_STORAGE_BUCKET_NAME
            path = obj.image.name
            return f"{base_url} / {bucket_name} / {path}"
        return None

class ProjectSerializer(serializers.ModelSerializer):
    technology_sections = TechnologySectionSerializer(many = True, read_only = True)
    project_images = ProjectImageSerializer(many = True, read_only = True) 

    class Meta:
        model = Project
        fields = "__all__"