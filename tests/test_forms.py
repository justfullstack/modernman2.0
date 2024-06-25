from customauth.forms import CustomUserCreationForm 
from django.core import mail
from django.test import TestCase




# class TestCustomAuthForms(TestCase):
#     """Tests custom authentication forms work as expoected"""
#     def testValidSignupFormSendsEmail(self):
#         """tests the form sends an email on successful submit"""
        
#         form = CustomUserCreationForm(
#                     {
#                         "email": "user1234@modernman.com",
#                         "password1": "abc@abcabc12!",
#                         "password2": "abc@abcabc12!",
#                     }
#                 )
        
#         self.assertTrue(form.is_valid())
        
#         with self.assertLogs("customauth.forms", level="INFO") as cm:
#             form.send_mail()
            
#             self.assertEqual(len(mail.outbox), 1)
            
#             self.assertEqual(
#                     mail.outbox[0].subject, 
#                     "Welcome to Modernman!"
#                 )
            
#         self.assertGreaterEqual(len(cm.output), 1)