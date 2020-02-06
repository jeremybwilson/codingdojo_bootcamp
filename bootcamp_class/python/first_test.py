import unittest

def sum_two(a, b):
  return a + b

def multiply_two(a, b):
  return a * b

class MainTester(unittest.TestCase):

  # methods that will test our functions

  # must begin with the word 'test'
  def test_hello(self):
    print("Hello")

    total = sum_two(13,7)
    self.assertEqual(total, 20)

    self.assertEqual(sum_two(100,200), 300)
    self.assertEqual(sum_two(1000,200), 1200)
    self.assertEqual(sum_two(1500,200), 1700)
    self.assertEqual(sum_two(-100,200), 100)

  #def test_goodbye(self):
  #  print("Goodbye")