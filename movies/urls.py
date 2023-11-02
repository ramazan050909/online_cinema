from rest_framework import routers

from movies.views import MovieViewSet, ActorViewSet, GenreViewSet

router = routers.DefaultRouter()
router.register('movies', MovieViewSet, basename='movies')
router.register('actors', ActorViewSet, basename='actors')
router.register('genres', GenreViewSet, basename='genres')

urlpatterns = router.urls