# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 00:48:01 2026

@author: jm172
"""

import random

words = ['яблоко', 'банан', 'апельсин', 'ананас', 'арбуз', 'виноград', 'клубника', 'кокос', 'лимно', 'манго', 'персик']
word = random.choice(words)
letters = []

chances = 6

print(f"Отгадайте слово! Это фрукт или ягода. У Вас есть {chances} попыток.")

letter_guessed = ['_'] * len(word)
for letter in letter_guessed:
    print(letter, end=' ')
print()

while letter_guessed != list(word) and chances > 0:
    guess = input('Введите букву: \n')
    if not guess.isalpha():
        print("Вы ввели число. Введите букву.")
        continue
    elif len(guess) > 1:
        print("Введите только одну букву.")
    elif guess in letters:
        print('Вы уже отгадывали эту букву.')
        continue
    
    letters.append(guess)
    
    if guess in word:
        print('Буква угадана!')
        for index, letter in enumerate(word):
            if letter == guess:
                letter_guessed[index] = letter
    else:
        print('Буква не угадана!')
        chances -= 1
    
    if letter_guessed == list(word) or chances == 0:
        continue
    
    print(f"У Вас осталось {chances} попыток.")
    
    for letter in letter_guessed:
        print(letter, end=' ')
    print()

if letter_guessed == list(word):
    print(f'Победа! Слово {word} отгадано!')
else:
    print(f'Поражение! Вы не отгадали слово {word}!')