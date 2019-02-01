# spiral.py
import turtle

# colors = ['dark red', 'DarkOrange', 'BlueViolet', 'MediumOrchid', 'yellow green', 'salmon', 'DeepPink', 'ForestGreen', 'MintCream', 'MistyRose']
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
l = len(colors)
r = 360 / l + 1

t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x % l])
    t.width(x / 100 + 1)
    t.forward(x / 2)
    t.left(r)
