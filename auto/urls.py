from django.contrib import admin
from django.urls import path, include
from common_views import auth_views, home

urlpatterns = [
    path('', home.home, name='home'),
    path('todo/', include("todo.urls")),
    path('admin/', admin.site.urls),
    #path("accounts/", include("django.contrib.auth.urls")),
    path('accounts/login', auth_views.login_view, name='login'),
    path('accounts/logout', auth_views.logout_user, name='logout'),
]
