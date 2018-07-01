from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import login,logout


urlpatterns = [
    url(r'^$', views.index,name='index'),
]
