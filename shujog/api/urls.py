from rest_framework.routers import DefaultRouter
from .views import UsersView


router = DefaultRouter()
router.register(r'userRegistration', UsersView, base_name="User Registrations")
urlpatterns = router.urls
