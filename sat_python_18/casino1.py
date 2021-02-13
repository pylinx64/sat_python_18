import random
print('Привет это казино три топора 777')
while True:
	number_random = random.randint(1, 10) # число
	number_player = input('Введите число: ')	# строка

	if number_random == int(number_player):
		print('$$$')
	else:
		print('--- Game over --')
		print(' =<( ')
	
