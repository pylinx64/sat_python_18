import turtle

t=turtle.Pen()
colors = ['black', 'yellow', 'lime']

t.speed('fastest')

for i in range(1000):
	t.pencolor(colors[i%3])
	t.left(36)
	t.forward(i)

turtle.done()
