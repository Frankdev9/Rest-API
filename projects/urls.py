from rest_framework import routers , permissions
from .api import ProjectViewset

route = routers.DefaultRouter()

route.register('api/projects',ProjectViewset,'projects')

# exporto las rutas
urlpatterns = route.urls
