# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 00:00:57 2026

@author: jm172
"""
import random

options = ["камень", "ножницы", "бумага"]

score_user = 0
score_computer = 0

while score_computer<3 and score_user <3:
    element = input("Введите элемент (камень, ножницы или бумага): ")
    option = random.choice(options)
    print(option)
    if element == option:
        print("Ничья")
    elif (
        (element == 'камень' and option == 'ножницы') 
        or (element == 'ножницы' and option == 'бумага')
        or (element == 'бумага' and option == 'камень')
        ):
        score_user += 1
        print("Победа")
    else:
        print("Проигрыш")
        score_computer += 1
    print(f"Счет: Пользователь {score_user} : Компьютер {score_computer}")
