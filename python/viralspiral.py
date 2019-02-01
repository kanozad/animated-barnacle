import turtle
t = turtle.Pen()
t.penup()
turtle.bgcolor("black")

sides = int(turtle.numinput("Number of sides", "How many sides in your spiral of spirals? (2-8)", 4, 2, 8))

colors = ['DarkOrange', 'BlueViolet', 'MediumOrchid', 'yellow green', 'salmon', 'DeepPink', 'ForestGreen', 'MintCream', 'MistyRose', 'dark red']

for m in range(100):
    t.forward(m*2)
    position = t.position()
    heading = t.heading()
    for n in range(int(m/4)):
        t.pendown()
        t.pencolor(colors[n%sides])
        t.forward(2*n)
        t.right(360/sides - 2)
        t.penup()
    t.setx(position[0])
    t.sety(position[1])
    t.setheading(heading)
    t.left(360/sides + 2)