import unittest
from category import Category

class TestCategory(unittest.TestCase):
  def test_nam_is_required(self):
    with self.assertRaisesRegex(TypeError, "missing 1 required positional argument: 'name'"):
      Category()

  def test_name_must_have_less_than_255_characters(self):
    long_name = "a" * 256
    with self.assertRaisesRegex(TypeError, "name must have less than 256 characters"):
      Category(long_name)

  

  def test_is_active_default_to_true(self):
    category = Category("name")
    self.assertTrue(category.is_active)


if __name__ == "__main__":
  unittest.main()