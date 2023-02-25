from rest_framework.routers import DefaultRouter
from TaskManager.views import TaskViewSet


router = DefaultRouter()

router.register(
        prefix="tasks",
        viewset=TaskViewSet,
        basename="tasks",
    )

urlpatterns = router.urls    
