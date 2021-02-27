import colorama
from colorama import Fore

colorama.init() 	
'''
print(Fore.LIGHTCYAN_EX + 'Start GTA 6...')

print(Fore.GREEN+'A', end='')
print(Fore.RED+'B', end='')
print(Fore.CYAN+'C', end='')
print(Fore.YELLOW+'D', end='')
'''

print(Fore.GREEN+'-> Вы бредете по лесу...')
print('-> *Через 1 час*')
print('-> В далеке замечаете огонь и лагерь рядом с ним')
print('-> Около лагеря вы встречаете волщебника с ооочень длинной бородой')
print(Fore.YELLOW+'-> Волшебник: я ждал тебя')
print('-> Волшебник: перед тобой стоят четыре портала')
print('-> *Указывает на порталы*')
print('-> Волшебник: в одном из них тебя ждут богатсва')
print('-> Волшебник: в остальных драконы')
print('-> Волшебник: какой портал ты выберешь')
print(Fore.CYAN)

import random
box = input('$ Введите номер портала: ')
box = int(box )						# превращает строку в число
box_random = random.randint(1, 4)

if box == box_random:
	print(Fore.GREEN+'-> Вы вошли в портал')
	print('...')
	print(Fore.WHITE+'------- ВЫ ВЫИГРАЛИ СОКРОВИЩА ------')

else:
	print(Fore.GREEN+'-> Вы вошли в портал')
	print('...')
	print(Fore.WHITE+'------- ВЫ ПРОИГРАЛИ СОКРОВИЩА ------')
