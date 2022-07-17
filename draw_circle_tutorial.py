import turtle
wn = turtle.Screen() .bgcolor("pink")

t = turtle.Turtle()
r = 10
n = 10
t.circle(r)
for i in range(1, n + 1, 1):
    t.circle(r * i)

wn.mainloop()