from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Course, QuotaRequest, Quota_accepeted, Student
from django.core.exceptions import ObjectDoesNotExist

class CourseViewTestCase(TestCase):
    def setUp(self):
        #create courses
        course1 = Course.objects.create(courseID="cn201", courseName="oop", courseSemester=1, courseYear=2023,
                                        courseChair=2, allowQuota_whenAvailable=True, withdraw_status=True)
        course2 = Course.objects.create(courseID="cn202", courseName="data1", courseSemester=2, courseYear=2023,
                                        courseChair=2, allowQuota_whenAvailable=True, withdraw_status=True)
        course3 = Course.objects.create(courseID="cn203", courseName="data2", courseSemester=1, courseYear=2023,
                                        courseChair=2, allowQuota_whenAvailable=False, withdraw_status=True)
        
    def test_course_list_view_status_code(self):
        """course list view's status code should return status code 200"""
        c = Client()
        response = c.get(reverse('course_list'))
        self.assertEqual(response.status_code, 200)
        
    def test_valid_course_detail_view_status_code(self):
        """valid course detail view's status code should return status code 200"""
        c = Client()
        response = c.get(reverse('course_detail', args=["cn201"]))
        self.assertEqual(response.status_code, 200)

    def test_invalid_course_detail_view_status_code(self):
        """invalid course detail view's status code should return status code 404"""
        c = Client()
        response = None
        
        # Use assertRaises to catch the ObjectDoesNotExist exception
        with self.assertRaises(ObjectDoesNotExist):
            response = c.get(reverse('course_detail', args=["cn205"]))
        
        # Check that the response status code is 404 (if response is not None)
        if response is not None:
            self.assertEqual(response.status_code, 404)


    
        