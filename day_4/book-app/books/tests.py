from django.test import TestCase
# Create your tests here.

# se pueden testear models y vistas

from .models import Category, Book, Author 

class CategoryModelsTest(TestCase):
    """ 
    Test for category model
    """

    def setUp(self):
        """
        Set up non-modified objects used by all test methods
        """
        Category.objects.create(name='test',description='test',status=True)
    
    def test_category_name_is_not_blank(self):
        """
        test for category name is nor blank
        """
        category = Category.objects.get(id=1)
        self.assertEqual(category.name,'test')
