from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "homeApp"

urlpatterns = [
    path('', views.homePage, name="home-page"),
    path('view/<int:id>', views.courseView, name="course-view"),
    path('courses/<str:courseType>/', views.allCourses, name="courses"),
    path('about-us/', views.about_us, name="about-us"),
    path('enroll-course/', views.enroll_function, name="enroll-course"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)