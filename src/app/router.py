from rest_framework import routers
from app.views.orang import OrangApiView
# from app.views.comment import CommentViewset
# from app.views.replies import RepliseViewSet

router = routers.DefaultRouter()
router.register('orang', OrangApiView, basename="orang")

app_url = router.urls