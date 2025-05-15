import unittest
from theory_of_computation.dfa import dfa_substring_101

class TestDFASubstring101(unittest.TestCase):

    def test_dfa(self):
        self.assertEqual(dfa_substring_101("101"), "Rejected")
        self.assertEqual(dfa_substring_101("0"), "Rejected")
        self.assertEqual(dfa_substring_101("11"), "Rejected")
        self.assertEqual(dfa_substring_101("1010"), "Accepted")
        self.assertEqual(dfa_substring_101("010101"), "Accepted")
        self.assertIsNone(dfa_substring_101("abc"))
        self.assertIsNone(dfa_substring_101("10#01"))
        self.assertEqual(dfa_substring_101("010"), "Rejected")

if __name__ == "__main__":
    unittest.main()

# if script 
# from theory_of_computation.dfa import dfa_substring_101

# def run_tests():
#     print("Running DFA tests...")
#     test_cases = [
#         ("101", "Accepted"),
#         ("0", "Rejected"),
#         ("11", "Rejected"),
#         ("1010", "Accepted"),
#         ("010101", "Accepted"),
#         ("abc", None),
#         ("10#01", None),
#         ("010", "Accepted")
#     ]

#     for input_string, expected in test_cases:
#         result = dfa_substring_101(input_string)
#         if result == expected:
#             print(f"Test passed for input: {input_string}")
#         else:
#             print(f"Test failed for input: {input_string}. Expected: {expected}, Got: {result}")

# if __name__ == "__main__":
#     run_tests()
