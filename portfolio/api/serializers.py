from rest_framework import serializers
from base.models import Project, ProjectImage, TechnologySection
from base.models import Project, TechnologySection, ProjectImage


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
        request = self.context.get("request")
        if obj.image and hasattr(obj.image, "url"):
            url = obj.image.url

            if request is not None:
                return request.build_absloute_uri(url)
            return url
        return None

class ProjectSerializer(serializers.ModelSerializer):
    technology_sections = TechnologySectionSerializer(many = True, read_only = True)
    project_images = ProjectImageSerializer(many = True, read_only = True) 

    class Meta:
        model = Project
        fields = "__all__"