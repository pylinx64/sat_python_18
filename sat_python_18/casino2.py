# библиотеки
import random
import time

# список
loot = ['Машина', 'баклажан', '40 грн', 'бензин', 'кирпич']

money = input('Введите кол-во денег > ')

while True:
	if int(money) > 10:
		# выбирает случайно из списка
		win_box = random.choice(loot)
		print(win_box)
		time.sleep(.3)
		# отнимает деньги
		money = int(money) - 10
	else:
		print('Бери кирпич в кредит (')
		# останавливает while True
		break
		
