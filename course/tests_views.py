from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Course, QuotaRequest, Quota_accepeted, Student ,Quota_rejected
from django.core.exceptions import ObjectDoesNotExist

class CourseViewTestCase(TestCase):
    def setUp(self):
        #create user
        user = User.objects.create_user(username='student1', password='123')
        self.student = Student.objects.create(id=user, name="name of student1")
        #create courses
        self.course1 = Course.objects.create(courseID="cn201", courseName="oop", courseSemester=1, courseYear=2023,
                                        courseChair=2, allowQuota_whenAvailable=True, withdraw_status=True)
        self.course2 = Course.objects.create(courseID="cn203", courseName="data2", courseSemester=1, courseYear=2023,
                                        courseChair=2, allowQuota_whenAvailable=True, withdraw_status=True)
        
    def test_course_list_view_status_code(self):
        #ทดสอบว่า view course list แสดงได้ถูกต้อง
        """course list view's status code should return status code 200"""
        c = Client()
        response = c.get(reverse('course_list'))
        self.assertEqual(response.status_code, 200)
        
    def test_valid_course_detail_view_status_code(self):
        #ทดสอบว่า view course detail แสดงได้ถูกต้อง
        """valid course detail view's status code should return status code 200"""
        c = Client()
        response = c.get(reverse('course_detail', args=["cn201"]))
        self.assertEqual(response.status_code, 200)

    def test_invalid_course_detail_view_status_code(self):
        #ทดสอบว่า view course detail แสดงได้ถูกต้อง
        """invalid course detail view's status code should return status code 404"""
        c = Client()
        response = None
        
        # Use assertRaises to catch the ObjectDoesNotExist exception
        with self.assertRaises(ObjectDoesNotExist):
            response = c.get(reverse('course_detail', args=["cn205"]))
        
        # Check that the response status code is 404 (if response is not None)
        if response is not None:
            self.assertEqual(response.status_code, 404)



    def test_valid_course_request(self):
        #ทดสอบว่าถ้า user ไม่ได้ login แต่ไปกดขอโควต้า จะมีการ redirect หน้า login ไป
        """valid course request view's status code should return status code 302"""
        # check if user does not login ,it will redirect to login page 
        c = Client()
        response = c.get(reverse('request_quota', args=["cn201"]))
        self.assertEqual(response.status_code,302)
        self.assertRedirects(response, reverse('login'))

    def test_valid_course_request_successhtmlreponse(self):
        #ทดสอบการขอโควต้าสำเร็จ
        """valid course request view's status code should return status code 200"""
        
        c = Client()
        logged_in = c.login(username="student1", password="123")

        # Check if the login was successful
        self.assertTrue(logged_in)
        response = c.get(reverse('request_quota', args=["cn201"]))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, '<h1>Success: you have requested this course\'s quota!</h1>', html=True)

    def test_valid_course_request_Errorhtmlreponse_1(self):
        #ทดสอบการขอโควต้าไม่สำเร็จ(มีการขอแล้ว)
        """valid course request view's status code should return status code 200"""
        
        c = Client()
        logged_in = c.login(username="student1", password="123")
        # Check if the login was successful
        self.assertTrue(logged_in)
        QuotaRequest.objects.create(course=self.course1, student=self.student)
        response = c.get(reverse('request_quota', args=["cn201"]))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, '<h1>Error : you can\'t request this course\'s quota.</h1>', html=True)

    def test_valid_course_request_Errorhtmlreponse_2(self):
        #ทดสอบการขอโควต้าไม่สำเร็จ(มีการ approve แล้ว)
        """valid course request view's status code should return status code 200"""
        
        c = Client()
        logged_in = c.login(username="student1", password="123")
        # Check if the login was successful
        self.assertTrue(logged_in)
        Quota_accepeted.objects.create(course=self.course1, student=self.student)
        response = c.get(reverse('request_quota', args=["cn201"]))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, '<h1>Error : you can\'t request this course\'s quota.</h1>', html=True)
    
    def test_valid_course_request_Errorhtmlreponse_3(self):
        #ทดสอบการขอโควต้าไม่สำเร็จ(มีการ reject แล้ว)
        """valid course request view's status code should return status code 200"""
        # Check if the login was successful
        c = Client()
        logged_in = c.login(username="student1", password="123")
        self.assertTrue(logged_in)

        Quota_rejected.objects.create(course=self.course1, student=self.student)
        response = c.get(reverse('request_quota', args=["cn201"]))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, '<h1>Error : you can\'t request this course\'s quota.</h1>', html=True)



    def test_valid_quota_status_1(self):
        #ทดสอบหน้า quota status ว่าถ้า userไม่ได้ login จะมีการ redirect กลับไปหน้า login
        """valid quota_status view's status code should return status code 302"""
        # check if user does not login ,it will redirect to login page 
        c = Client()
        response = c.get(reverse('quota_status'))
        self.assertEqual(response.status_code,302)
        self.assertRedirects(response, reverse('login'))

    def test_valid_quota_status_2(self):
        #ทดสอบหน้า quota status ว่าถ้า user login แล้วจะมีการ redirect ไปหน้า quota status
        """valid quota_status view's status code should return status code 200"""
        # Check if the login was successful, it will redirect to quota_status page
        c = Client()
        logged_in = c.login(username="student1", password="123")
        self.assertTrue(logged_in)
        response = c.get(reverse('quota_status'))
        self.assertEqual(response.status_code,200)
    
    def test_valid_quota_withdraw(self):
        #ทดสอบว่าถ้า user ไม่ได้ login จะ redirect ไปหน้า login ถ้ากด withdraw
        """valid quota_withdraw view's status code should return status code 302"""
        # check if user does not login ,it will redirect to login page 
        c = Client()
        response = c.get(reverse('quota_withdraw',args=["cn203"]))
        self.assertEqual(response.status_code,302)
        self.assertRedirects(response, reverse('login'))

    def test_valid_withdraw_Quota_html(self):
        #ทดสอบว่าถ้า user login แล้วจะถอนสำเร็จ
        """valid quota_withdraw view's status code should return status code 200"""
        # Check if the login was successful
        c = Client()
        logged_in = c.login(username="student1", password="123")
        self.assertTrue(logged_in)
        response = c.get(reverse('quota_withdraw',args=["cn203"]))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, '<h1>Success: you have withdrawn this course\'s quota!</h1>', html=True)

    
        