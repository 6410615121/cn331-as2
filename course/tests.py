from django.test import TestCase
from .models import Course, QuotaRequest

# Create your tests here.

class CourseTestCase(TestCase):
    def setUp(self):
        #create courses
        course1 = Course.objects.create(courseID="cn201", courseName="oop", courseSemester=1, courseYear=2023,
                                        courseChair=3, allowQuota_whenAvailable=True, withdraw_status=True)
        course2 = Course.objects.create(courseID="cn202", courseName="data1", courseSemester=2, courseYear=2023,
                                        courseChair=3, allowQuota_whenAvailable=True, withdraw_status=True)
        course3 = Course.objects.create(courseID="cn203", courseName="data2", courseSemester=1, courseYear=2023,
                                        courseChair=3, allowQuota_whenAvailable=True, withdraw_status=True)
        
    def test_chair_available(self):
        """ is_chair_available should be True """
                                        