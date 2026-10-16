#import unittest
#class TestContactApp(unittest.TestCase):

 #           OR

from unittest import TestCase

from contact_app_functions import create_contact, clear_contacts

class TestContactApp(TestCase):


    def test_that_new_contact_can_be_created_and_saved(self):
        clear_contacts()

        first_name = "Daniel"
        last_name = "messaih"
        phone_number = "09076583512"


        contact = create_contact(first_name, last_name, phone_number)

        self.assertEqual(type(contact), list)
        self.assertEqual(len(contact), 3)

        self.assertEqual("09076583512", contact[-1])


    def test_that_duplicate_contacts_cannot_be_created(self):
        clear_contacts()

        first_name = "john"
        last_name = "job"
        phone_number = "09076583512"


        contact = create_contact(first_name, last_name, phone_number)


        first_name = "james"
        last_name = "Mattew"
        phone_number = "09076583512"


        contact = create_contact(first_name, last_name, phone_number)

        self.assertIsNone(contact)
