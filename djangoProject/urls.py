"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from blog.views import PostViewSet
from categories.views import CategoryViewSet
from comments.views import CommentViewSet
from djangoProject import settings
from tags.views import TagViewSet
from levels.views import LevelViewSet
from users.views import RegisterView
from votes.views import VoteViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('tags', TagViewSet)
router.register('comments', CommentViewSet)
router.register('votes', VoteViewSet)
router.register('categories', CategoryViewSet)
router.register('levels', LevelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/register', RegisterView.as_view(), name='register'),
    path('__debug__/', include('debug_toolbar.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
