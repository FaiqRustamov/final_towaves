from django.urls import path, include, reverse
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from blog.views import login,join, eventcreate

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'blog', BlogViewSet)


app_name = 'blog'

urlpatterns = [
    path('categories/', categories, name="categories"),
    path('userpanel/', user_panel, name="userpanel"),
    path('comment/', commentuser, name="comment"),
    path('logout/', logout, name="logout"),
    path('userevent/', event_user_page, name="event_user"),
    path('create/', EventCreate.as_view(), name="create_event"),
    path('register/', register, name="reg"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', homepage, name='home'),
    path('signup/', signup, name='signup'),
    path('success/', Success, name='success'),
    path('contactus/', Contact, name='contact'),
    path('login/', login, name="login"),
    path('join/', JoinAjaxView.as_view(), name="join"),
    path('description/', description, name = 'description')
]