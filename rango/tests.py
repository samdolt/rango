from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from rango.models import Category, Page
from django.db.utils import IntegrityError

class ModelCategoryTests(TestCase):

    def test_str_method(self):
        category = Category(name="Hello")
        self.assertEqual(str(category), "Hello")

    def test_get_name(self):
        category = Category(name="World")
        self.assertEqual(category.name, "World")


class ModelPageTests(TestCase):

    def test_save_blank_field(self):
        """
        Page as some required field
        """
        page = Page()
        with self.assertRaises(IntegrityError):
            page.save()
            page.title = "Hello"
            page.category = Category(name="Hello")
            page.
    def test_init_method_with_all_arg(self):
        page = Page()


    def test_str_method(self):
        page = Page()
        return


class ViewIndexTests(TestCase):

    def test_index_response(self):
        c = Client()
        response = c.get(reverse("rango:index"))
        self.assertEquals(response.status_code, 200)
