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
            public_base_url = "https://pub-7690719314794044b6cc954361c5e563.r2.dev"
            bucket = settings.AWS_STORAGE_BUCKET_NAME.strip("/")
            file_path = obj.image.name.strip("/")
            return f"{public_base_url}/{bucket}/{file_path}"
        return None

class ProjectSerializer(serializers.ModelSerializer):
    technology_sections = TechnologySectionSerializer(many = True, read_only = True)
    project_images = ProjectImageSerializer(many = True, read_only = True) 

    class Meta:
        model = Project
        fields = "__all__"