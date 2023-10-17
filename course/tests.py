from django.test import TestCase
from django.contrib.auth.models import User
from .models import Course, QuotaRequest, Quota_accepeted, Student

# Create your tests here.

class CourseTestCase(TestCase):
    def setUp(self):
        #create courses
        course1 = Course.objects.create(courseID="cn201", courseName="oop", courseSemester=1, courseYear=2023,
                                        courseChair=2, allowQuota_whenAvailable=True, withdraw_status=True)
        course2 = Course.objects.create(courseID="cn202", courseName="data1", courseSemester=2, courseYear=2023,
                                        courseChair=2, allowQuota_whenAvailable=True, withdraw_status=True)
        course3 = Course.objects.create(courseID="cn203", courseName="data2", courseSemester=1, courseYear=2023,
                                        courseChair=2, allowQuota_whenAvailable=False, withdraw_status=True)

        
    def test_chair_available(self):
        """ is_chair_available should be True """
        course = Course.objects.get(courseID = "cn201")
        self.assertTrue(course.is_chair_available())

    def test_chair_not_available(self):
        """ is_chair_available should be False """
        course = Course.objects.get(courseID = "cn201")

        #create student user
        user1 = User.objects.create_user(username='student1', password='123')
        student1 = Student.objects.create(id=user1, name="name of student1")
        
        user2 = User.objects.create_user(username='student2', password='123')
        student2 = Student.objects.create(id=user2, name="name of student2")

        Quota_accepeted.objects.create(course=course, student=student1)
        Quota_accepeted.objects.create(course=course, student=student2)
        self.assertFalse(course.is_chair_available())

    def test_quota_status1(self):
        #admin open quota requesting And chair is available
        """is_quota_status_open should be True"""
        course = Course.objects.get(courseID = "cn201")
        self.assertTrue(course.is_quota_status_open())

    def test_quota_status2(self):
        #admin open quota requesting And chair is not available
        """is_quota_status_open should be False"""
        course = Course.objects.get(courseID = "cn201")

        #create student user
        user1 = User.objects.create_user(username='student1', password='123')
        student1 = Student.objects.create(id=user1, name="name of student1")
        
        user2 = User.objects.create_user(username='student2', password='123')
        student2 = Student.objects.create(id=user2, name="name of student2")

        Quota_accepeted.objects.create(course=course, student=student1)
        Quota_accepeted.objects.create(course=course, student=student2)
        self.assertFalse(course.is_quota_status_open())

    def test_quota_status3(self):
        #admin close quota requesting
        """is_quota_status_open should be False"""
        course = Course.objects.get(courseID = "cn203")
        self.assertFalse(course.is_quota_status_open())
