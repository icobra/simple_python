#!/usr/bin/python3

"""
Simple math game - choose quickly
"""

from random import randint
from random import choice

def make_unknown(computer_number, result, operation):
    if operation == "+":
        return result - computer_number
    if operation == "-":
        return result + computer_number
    # For future
    if operation == "*":
        return result // computer_number
    if operation == "//":
        return result * computer_number

def guess():
    # Check user input and return correct answer
    while True:
        number = input("Press 'e(xit)' or any to return...")
        if number == 'e':
            exit()
        else:
            return

def main():
    while True:
        # Создать два случайных числа
        computer_number = randint(0, 100)
        result = randint(0, 100) 
        # Выбрать случайное действие
        operation_list = ["+", "-"]
        operation = choice(operation_list)
        unknown = make_unknown(computer_number, result, operation)
        # Создать выражение
        print ("Find X:")
        print ("x", operation, computer_number, " = ", result)
        # Попросить пользователя найти решение
        answer = input("Input answer: ")

        # Проверить верен ли ответ
        if int(answer) == int(unknown):
            print("You win")
        else:
            print("You lose. Right answer is ...", unknown )
        guess()

if __name__ == "__main__":
    main()
