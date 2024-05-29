import unittest
from app.calculator import evaluate_expression, add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_evaluate_expression(self):
        self.assertEqual(evaluate_expression("2+3"), 5)
        self.assertEqual(evaluate_expression("2-3"), -1)
        self.assertEqual(evaluate_expression("2*3"), 6)
        self.assertEqual(evaluate_expression("6/3"), 2)
        self.assertIn("by zero", evaluate_expression("6/0"))


    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(2, 3), -1)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(6, 0), "Error: Division by zero")

if __name__ == '__main__':
    unittest.main()

