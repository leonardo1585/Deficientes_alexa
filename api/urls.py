from django.contrib import admin
from django.urls import path, include
from core.views import PessoaViewSet
from rest_framework import routers
from django_ask_sdk.skill_adapter import SkillAdapter
import Deficientes_alexa


router = routers.DefaultRouter()
router.register(r'pessoas', PessoaViewSet)
view = SkillAdapter.as_view(skill=Deficientes_alexa.sb.create())
# router.register(r'helloworld', LaunchRequestHandler)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('lugar', view, name='index')
]
