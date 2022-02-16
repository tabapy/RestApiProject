from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter
from forum_settings import settings
from main.views import CategoryListView, PostsViewSet, PostImageView, CommentViewSet, LikesViewSet, RatingViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="FISHING FORUM",
        description='FORUM FOR PROFESSIONAL FISHERMANS',
        default_version='v1'
    ),
    public=True
)
router = DefaultRouter()
router.register('posts', PostsViewSet)
router.register('comments', CommentViewSet)
router.register('likes', LikesViewSet)
router.register('rating', RatingViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger')),
    path('api-auth/', include('rest_framework.urls')),
    path('v1/api/categories/', CategoryListView.as_view()),
    path('v1/api/add-image/', PostImageView.as_view()),
    path('v1/api/account/', include('account.urls')),
    path('v1/api/', include(router.urls)),
    path('v1/api/chat/', include('chat.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)