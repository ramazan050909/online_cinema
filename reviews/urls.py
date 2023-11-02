from rest_framework.routers import DefaultRouter
# from django.urls import path, include
from .views import CommentViewSet, RatingViewSet, FavoriteViewSet, LikeViewSet

router = DefaultRouter()
router.register('comment', CommentViewSet, 'comment')
router.register('ratings', RatingViewSet, 'ratings')
router.register('favorites', FavoriteViewSet, 'favorite')
router.register('likes', LikeViewSet, 'like')

urlpatterns = router.urls