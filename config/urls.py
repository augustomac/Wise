from django.contrib import admin
from django.urls import path, include
from estoque.views import ItemViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'itens', ItemViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]