from email.policy import default
from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    short_description = models.TextField()
    description = models.TextField()
    course_old_fee = models.IntegerField(default=0)
    course_fee = models.IntegerField(default=0)
    course_photo = models.ImageField(upload_to='corusPhoto', default="corusPhoto\image-not-found.jpg")
    running = models.BooleanField(default=False)
    def __str__(self):
        return self.course_name

    class Meta:
        db_table = 'Courses'
    
class CourseDetails(models.Model):
    course_id = models.OneToOneField(Course, on_delete=models.CASCADE)
    heading_first = models.CharField(max_length=255)
    heading_firs_description = models.TextField()
    heading_second = models.CharField(max_length=255)
    heading_second_description = models.TextField()
    list_first = models.CharField(max_length=255)
    list_first_description = models.TextField()
    list_second = models.CharField(max_length=255)
    list_second_description = models.TextField()
  

    def __str__(self):
        return str(self.course_id.course_name) + " Details"

    class Meta:
        db_table = 'Course Details'

    


