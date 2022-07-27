from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'userAuthentication'

urlpatterns = [
    path('login/', views.loginPage, name="login-page"),
    path('register/', views.register, name="register-page"),
    path('user_login/', views.user_login, name="user-login"),
    path('logout/', views.user_logout, name="user-logout"),
    path('profile/', views.profile, name="profile"),
    path('update-profile/<int:id>', views.update_profile, name='update-profile'),
    path('set-profile-image/<int:id>', views.set_profile_image, name='set-profile-image'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)