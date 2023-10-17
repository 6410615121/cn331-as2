from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Course, QuotaRequest, Quota_accepeted, Student

class CourseViewTestCase(TestCase):
    def setUp(self):
        #create courses
        course1 = Course.objects.create(courseID="cn201", courseName="oop", courseSemester=1, courseYear=2023,
                                        courseChair=2, allowQuota_whenAvailable=True, withdraw_status=True)
        course2 = Course.objects.create(courseID="cn202", courseName="data1", courseSemester=2, courseYear=2023,
                                        courseChair=2, allowQuota_whenAvailable=True, withdraw_status=True)
        course3 = Course.objects.create(courseID="cn203", courseName="data2", courseSemester=1, courseYear=2023,
                                        courseChair=2, allowQuota_whenAvailable=False, withdraw_status=True)
        
    def test_index_view_status_code(self):
        """index view's status code is ok"""
        c = Client()
        response = c.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        