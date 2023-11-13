import unittest
from math_quiz import generateInteger, chooseOperator, calculation
class TestMathGame(unittest.TestCase):

    def test_generateInteger(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generateInteger(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_chooseOperator(self):
        # TODO
        # Test if the function chooseOperator works
        operator = chooseOperator()
        valid_operator = {'+', '-', '*'}
        self.assertIn(operator, valid_operator, f"Generated operator '{operator}' is not in '{valid_operator}'")


    def test_calculation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7), (7, 4, '-', '7 - 4', 3), (2, 3, '*', '2 * 3', 6)
                ''' TODO add more test cases here '''
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # To align variable name for the numbers and operators in cases
                with self.subTest(num1 = num1, num2 = num2, operator = operator, expected_problem = expected_problem,
                                  expected_answer = expected_answer):
                # use subTest for identifying the differences from one case to another
                    problem, correctAnswer = calculation(num1, num2, operator)
                # calculate these cases
                    self.assertEqual(problem, expected_problem,
                                     f"The test of problem {num1} {operator} {num2} is not passed")
                # test the problem by comparing problem and expected_problem
                    self.assertEqual(correctAnswer, expected_answer,
                                     f"The test of answer for {num1} {operator} {num2} is not passed")
                # test if the calculated answer right, and comparing.


if __name__ == "__main__":
    unittest.main()
