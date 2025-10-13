from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Project
from .serializers import ProjectSerializer
  

@api_view(["GET", "HEAD"])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many = True)
    return Response(serializer.data)
