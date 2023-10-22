from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
from .models import Course ,QuotaRequest ,Student ,Quota_accepeted ,Quota_rejected

class StudentAdminTestCase(TestCase):
    def setUp(self):
        # Create a superuser 
        self.admin_user = User.objects.create_superuser(username='root', password='1234')
        self.student = Student.objects.create(id=self.admin_user, name="name of student")
        self.course1 = Course.objects.create(courseID="cn201", courseName="oop", courseSemester=1, courseYear=2023,
                                        courseChair=2, allowQuota_whenAvailable=True, withdraw_status=True)
        self.course2 = Course.objects.create(courseID="cn202", courseName="data1", courseSemester=2, courseYear=2023,
                                        courseChair=2, allowQuota_whenAvailable=True, withdraw_status=True)
        self.qr = QuotaRequest.objects.create(course=self.course1, student=self.student)


    def test_course_admin_Course_display(self):
        #ทดสอบหน้า admin course display 
        c = Client()
        logged_in = c.login(username='root', password='1234')
        self.assertTrue(logged_in)

        response = c.get('/admin/course/course/')  

        self.assertContains(response, 'courseID')
        self.assertContains(response, 'courseName')
        self.assertContains(response, 'availableChairs')
    
    def test_course_admin_QuotaRequest_display(self):
        #ทดสอบหน้า admin quotarequest display 
        c = Client()
        logged_in = c.login(username='root', password='1234')
        self.assertTrue(logged_in)

        response = c.get('/admin/course/quotarequest/')  

        self.assertContains(response, 'course')
        self.assertContains(response, 'student')
        self.assertContains(response, 'requestID')
    
    def test_withdraw_accepted_quota_action(self):
        #ทดสอบ action withdraw quota ที่ได้รับการ approve แล้ว
        # Create some QuotaRequest objects for testing
        Quota_accepeted_1 = Quota_accepeted.objects.create(course=self.course1, student=self.student)
        

        client = Client()
        client.login(username='root', password='1234')

        data = {
            '_selected_action': [Quota_accepeted_1.pk],  # Select the objects to act on
            'action': 'withdraw',  # action
        }

        response = client.post('/admin/course/quota_accepeted/', data) 
        # Assert that the QuotaRequest objects should have been deleted
        self.assertFalse(QuotaRequest.objects.filter(pk=Quota_accepeted_1.pk).exists())



    def test_approve_requests_action(self):
        #ทดสอบ action การ approve quota
        # Create some QuotaRequest objects for testing
        quota_request_1 = QuotaRequest.objects.create(course=self.course1, student=self.student)

        client = Client()
        client.login(username='root', password='1234')

        data = {
            '_selected_action': [quota_request_1.pk],  # Select the objects to act on
            'action': 'approve_requests',  # action
        }

        response = client.post('/admin/course/quotarequest/', data)

        # Assert that the QuotaRequest objects should have been deleted
        self.assertFalse(QuotaRequest.objects.filter(pk=quota_request_1.pk).exists())

        # Assert that QuotaAccepted objects should have been created as expected
        self.assertTrue(Quota_accepeted.objects.filter(course=self.course1, student=self.student).exists())

    def test_reject_requests_action(self):
        #ทดสอบ action การ reject quota
        # Create some QuotaRequest objects for testing
        quota_request_1 = QuotaRequest.objects.create(course=self.course1, student=self.student)

        client = Client()
        client.login(username='root', password='1234')

        data = {
            '_selected_action': [quota_request_1.pk],  # Select the objects to act on
            'action': 'reject_requests',  # action
        }

        response = client.post('/admin/course/quotarequest/', data)

        # Assert that the QuotaRequest objects should have been deleted
        self.assertFalse(QuotaRequest.objects.filter(pk=quota_request_1.pk).exists())

        # Assert that Quota_rejected objects should have been created as expected
        self.assertTrue(Quota_rejected.objects.filter(course=self.course1, student=self.student).exists())
        


    def test_course_admin_Quotaaccepete_display(self):
        #ทดสอบการแสดงหน้า course admin quota accepted display
        c = Client()
        logged_in = c.login(username='root', password='1234')
        self.assertTrue(logged_in)

        response = c.get('/admin/course/quota_accepeted/')  

        self.assertContains(response, 'course')
        self.assertContains(response, 'student')


    def test_course_admin_Quotarejected_display(self):
        #ทดสอบการแสดงหน้า course admin quota rejected display
        c = Client()
        logged_in = c.login(username='root', password='1234')
        self.assertTrue(logged_in)

        response = c.get('/admin/course/quota_rejected/')  

        self.assertContains(response, 'course')
        self.assertContains(response, 'student')

    
    