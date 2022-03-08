from django.urls import path, include
from django.contrib.auth import views
from django.contrib import admin
from blog import views as default_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', default_views.signUp, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/register/', views.RegisterView.as_view(), name='register'),
    # path('accounts/login/', views.LoginView.as_view(), name='login'),
    # path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', include('blog.urls')),
]