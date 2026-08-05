# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - закрыть программу."""


tasks = {}

while True:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату, которую нужно отобразить: ")
        if date in tasks:
            print(f"Планы на дату {date}")
            for task_date in tasks[date]:
                print("- ", task_date)
        else:
            print("Такой даты нет!")
            continue
    elif command == "add":
        date = input("Введите дату: ")
        task = input("Введите название задачи: ")
        if date in tasks:
            tasks[date].append(task)
        else:
            tasks[date] = []
            tasks[date].append(task)
        print(f"Задача {task} добавлена")
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная команда. Введите валидную команду.")
        continue
        