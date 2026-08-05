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


# today = []
# tomorrow = []
# other = []

tasks = {}

while True:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print("Планы: \n", tasks)
        # print("Сеогдня\n", today)
        # print("Завтра\n", tomorrow)
        # print("Другие\n", other)
    elif command == "add":
        date = input("Введите дату: ")
        task = input("Введите название задачи: ")
        if date in tasks:
            tasks[date].append(task)
        else:
            tasks[date] = []
            print(tasks)
            tasks[date].append(task)
        # if date == "Сегодня":
        #     today.append(task)
        # elif date == "Завтра":
        #     tomorrow.append(task)
        # else:
        #     other.apend(task)
        print(f"Задача {task} добавлена")
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная команда. Введите валидную команду.")
        continue
        