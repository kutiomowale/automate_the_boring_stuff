#!/usr/bin/env python3
# Multiplication Quiz 2
# Practice Project
# Without using pyinputplus
import random
import time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    numberOfTries = 0
    while True:
        print('#%s: %s x %s = ' % (questionNumber, num1, num2), end='')
        numberOfTries += 1
        if numberOfTries > 3:
            print('Out of tries')
            break
        try:
            response = int(input())
        except ValueError:
            print("Only Integers")
            continue
        else:
            if response == num1 * num2:
                print('Correct!')
                correctAnswers += 1
                break
            else:
                print('Incorrect!')
    time.sleep(1)  # Brief pause to let user see the result.
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))
