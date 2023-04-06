from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_create_menu(self):
        # Create a new Menu object
        menu = Menu.objects.create(title="IceCream", price=80, inventory=100)
        # Check that the string representation of the Menu object matches our expectation
        self.assertEqual(menu, "IceCream : 80")