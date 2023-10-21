from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Student

class UsersViewTestCase(TestCase):
    def setUp(self):
        #create user
        user = User.objects.create_user(username='student', password='123')
        self.student = Student.objects.create(id=user, name="name of student1")
    

    def test_valid_index_1(self):
        """valid index view's status code should return status code 302"""
        # check if user does not login ,it will redirect to login page 
        c = Client()
        response = c.get(reverse('index'))
        self.assertEqual(response.status_code,302)
        self.assertRedirects(response, reverse('login'))

    def test_valid_index_2(self):
        """valid index view's status code should return status code 200"""
        
        c = Client()
        logged_in = c.login(username="student", password="123")

        # Check if the login was successful
        self.assertTrue(logged_in)
        response = c.get(reverse('index'))
        self.assertEqual(response.status_code,200)


    def test_valid_login(self):
        """valid login view's status code should return status code 200"""
        
        c = Client()
        response = c.post(reverse('login'), {'username': 'student', 'password': '123'})
        self.assertEqual(response.status_code,302)
        self.assertRedirects(response, reverse('index'))

    def test_invalid_login(self):
        """invalid login view's status code should return status code 302"""
        
        c = Client()
        response = c.post(reverse('login'), {'username': 'student', 'password': '124'})
        self.assertEqual(response.status_code,200)
        # it will render login html
    
    def test_valid_logout(self):
        """valid logout view's status code should return status code 200"""
        # check if user does not login ,it will redirect to login page 
        c = Client()
        response = c.get(reverse('logout'))
        self.assertEqual(response.status_code,200)
     
        