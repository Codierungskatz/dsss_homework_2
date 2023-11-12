import random


def generateInteger(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def chooseOperator():
    return random.choice(['+', '-', '*'])


def calculation(num_1, num_2, operator):   # rename o: operator n1: num_1  n2: num_2
    # rename: function ABC
    performance = f"{num_1} {operator} {num_2}"
    if operator == '+':
        answer = num_1 + num_2  # wrong operators
    elif operator == '-':
        answer = num_1 - num_2
    else:
        answer = num_1 * num_2
    return performance, answer

def math_quiz():
    score = 0
    # s = 0
    # t_q = 3.14159265359
    totalNumberOfQuestions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(totalNumberOfQuestions):
        num_1 = generateInteger(1, 10)
        num_2 = generateInteger(1, 5)  # 5.5 is unacceptable for random.randint
        operator = chooseOperator()
        problem, correctAnswer = calculation(num_1, num_2, operator)
        # PROBLEM, ANSWER = calculation(num_1, num_2, operator)
        print(f"\nQuestion: {problem}")
        getUserAnswer = input("Your answer: ")  # rename
        userAnswer = int(getUserAnswer)

        if userAnswer == correctAnswer:
            print("Correct! You earned a point.")
            score += 1     # directly 1
        else:
            print(f"Wrong answer. The correct answer is {correctAnswer}.")

    print(f"\nGame over! Your score is: {score}/{totalNumberOfQuestions}")

if __name__ == "__main__":
    math_quiz()
