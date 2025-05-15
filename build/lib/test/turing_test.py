from theory_of_computation.turing_machine_divisible_by_3 import turing_machine_divisible_by_3
import unittest

class TestDivisibility(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(turing_machine_divisible_by_3("0"), True)
        self.assertEqual(turing_machine_divisible_by_3("11"), True)
        self.assertEqual(turing_machine_divisible_by_3("110"), True)
        self.assertEqual(turing_machine_divisible_by_3("10"), False)

if __name__ == "__main__":
    unittest.main()

# if script
# def run_tests():
#     print("Running Turing Machine tests...")

#     test_cases = [
#         ("110", True),
#         ("101", False),
#         ("111", True),
#         ("1001", False),
#         ("0", True),
#         ("abc", None),
#         ("10#01", None),
#         ("11", False)
#     ]

#     for input_string, expected in test_cases:
#         result = turing_machine_divisible_by_3(input_string)
#         if result == expected:
#             print(f"Test passed for input: {input_string}")
#         else:
#             print(f"Test failed for input: {input_string}. Expected: {expected}, Got: {result}")

# if __name__ == "__main__":
#     run_tests()
