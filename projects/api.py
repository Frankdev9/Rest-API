from rest_framework import viewsets , permissions
from .models import Project
from .serializers import ProjectSerializers


class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializers
    # permissions_classes=[permissions.AllowAny]
    # Esta linea te dice que cualquier usuario puede interactuar con esta vista 
