# Задача 2
# from os import system
# system("cls")
# import random

# def get_number(input_string:str)->int:
#     '''
#     Получение количества конфет
#     '''
#     while True:
#         try:
#             num = int(input(input_string))
#             if 0 < num < 29:
#                 return num
#             else:
#                 print('Неправильно. Давай еще раз.')
#         except ValueError:
#             print('Это не то ...')

# def last_move(input_string:str, number:int)->int:
#     '''
#     Получение количества конфет
#     для последнего хода
#     '''
#     while True:
#         try:
#             num = int(input(input_string))
#             if 0 < num <= number:
#                 return num
#             else:
#                 print('Неправильно. Давай еще раз.')
#         except ValueError:
#             print('Это не то ...')

# def get_player(player_0:str, player_1:str)->str:
#     '''
#     Получение имени игроков
#     определение первого хода
#     '''
#     print('Сейчас мы разыграем право первого хода...')
#     temp = random.randint(0, 1)
#     if temp == 0:
#         gamer = player_0
#     else:
#         gamer = player_1
#     print(f'И первым у нас берет конфеты {gamer}!')
#     return gamer

# def playng(candy:int, player:str, player_1:str, player_2:str)->str:
#     winner = ''
#     while candy > 0:
#         if candy > 28:
#             if player == player_1:
#                 print(f'У нас {candy} конфет.')
#                 move = get_number(f'{player} сколько вы берете кофет? Вы можете взять от 1 до 28: ')
#                 candy -= move
#                 player = player_2
#                 winner = player_1
#             else:
#                 print(f'У нас {candy} конфет.')
#                 move = get_number(f'{player} сколько вы берете кофет? Вы можете взять от 1 до 28: ')
#                 candy -= move
#                 player = player_1
#                 winner = player_2
#         else:
#             if player == player_1:
#                 print(f'У нас {candy} конфет.')
#                 move = last_move(f'{player} сколько вы берете кофет? Вы можете взять от 1 до {candy}: ', candy)
#                 candy -= move
#                 player = player_2
#                 winner = player_1
#             else:
#                 print(f'У нас {candy} конфет.')
#                 move = last_move(f'{player} сколько вы берете кофет? Вы можете взять от 1 до {candy}: ', candy)
#                 candy -= move
#                 player = player_1
#                 winner = player_2
#     return winner


# print('''
# Добро пожаловать в игру "Sweet Life".
# Правила нашей игры:
# На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Выигрывает игрок сделавший последний ход 
# - он забирает все конфеты.\n''')

# name_0 = input('''Давайте знакомиться. Первый игрок, как к Вам обращаться?\n''')
# name_1 = input('Второй игрок, представтесь, пожалуйста:\n')
# gamer = get_player(name_0, name_1)
# sweet = 200
# winner = playng(sweet, gamer, name_0, name_1)
# print(f'''
# У нас есть победитель.
# Это {winner}!!!
# Наша игра закончена.''') 

# Задача 1
# def del_word():
#     '''
#     Функция удаляет слово если в ней есть определенный участок
#     '''
#     line = 'абвгдейка - это передача'
#     words = line.split(' ')
#     fragment = 'абв'
#     new_words = []
#     for word in words:
#         if fragment not in word:
#             new_words.append(word)
#     new_words = ' '.join(new_words)
#     print(new_words)
# del_word()

# Задача 3
# from os import system
# system("cls")

# def select(f, col):
#     return [f(x) for x in col]

# def get_list(list_tuple:list)->list:
#     list_output_2 = []
#     for element in list_output_1:
#         number = sum(select(lambda x: ord(x), element[1]))
#         if number % element[0] == 0:
#             list_output_2.append((number, element[1]))
#     return list_output_2



# list_input_1 = ['Java', 'C', 'Python', 'C++', 'Go', 'C#', 'Fortran', 'JavaScript', 'PHP', 'Scratch']
# list_input_2 = [i for i in range(1, len(list_input_1) + 1)]
# list_output_1 = list(zip(list_input_2, select(lambda x: x.upper(), list_input_1)))
# print(list_output_1)
# list_output_2 = get_list(list_output_1)
# print(list_output_2)