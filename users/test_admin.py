from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
from .models import Student  

class StudentAdminTestCase(TestCase):
    def setUp(self):
        # Create a superuser 
        self.admin_user = User.objects.create_superuser(username='root', password='1234')
        self.student = Student.objects.create(id=self.admin_user, name="name of student") 

    def test_student_admin_list_display(self):
        #ทดสอบการแสดงหน้า student admin list
        c = Client()
        logged_in = c.login(username='root', password='1234')
        self.assertTrue(logged_in)

        response = c.get('/admin/users/student/')  

        self.assertContains(response, 'id')
        self.assertContains(response, 'name')

    