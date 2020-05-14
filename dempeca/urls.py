from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register(r'demandas', views.DemandaViewSet)
router.register(r'pecas', views.PecaViewSet)
router.register(r'usuarios', views.UsuarioViewSet)
