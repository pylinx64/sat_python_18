from mcpi.minecraft import Minecraft
import random

# подключаемся и храним сервер
server = Minecraft.create()

# координаты и id
x = 123
y = 69
z = 129
block = 46

for y in range(y, 256):
	print(y)
	
	# ставим блок 
	server.setBlock(x, y, z, random.randint(1, 120))
