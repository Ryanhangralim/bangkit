import unittest

# from rearrange import rearrange_name

# class TestRearrange(unittest.TestCase):
    
#     def test_basic(self):
#         testcase = "Lovelace, Ada"
#         expected = "Ada Lovelace"
#         self.assertEqual(rearrange_name(testcase), expected)

#     def test_empty(self):
#         testcase = ""
#         expected = ""
#         self.assertEqual(rearrange_name(testcase), expected)

#     def test_double_name(self):
#         testcase = "Hopper, Grace M."
#         expected = "Grace M. Hopper"
#         self.assertEqual(rearrange_name(testcase), expected)

#     def test_one_name(self):
#         testcase = "Voltaire"
#         expected = "Voltaire"
#         self.assertEqual(rearrange_name(testcase), expected)

# # Run the tests
# unittest.main()

# class TestStringMethods(unittest.TestCase):


#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')


#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())


#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError): 
#             s.split(2)


# if __name__ == '__main__':
#     unittest.main()

import unittest

from try_except import validate_user

class TestValidateUser(unittest.TestCase):
  def test_valid(self):
    self.assertEqual(validate_user("validuser", 3), True)

  def test_too_short(self):
    self.assertEqual(validate_user("inv", 5), False)

  def test_invalid_characters(self):
    self.assertEqual(validate_user("invalid_user", 1), False)
  def test_invalid_minlen(self):
    self.assertRaises(ValueError, validate_user, "user", -1)


# Run the tests
unittest.main()
