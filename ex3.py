# Homework2
import turtle
import turtle as t
t.shape('turtle')
s = 50
a = 90
p = 30
n = int(input())
for i in range(n):
    for i in range(4):
        t.forward(s)
        t.left(a)
        t.penup()
        t.backward(p/2)
        t.right(a)
        t.forward(p/2)
        t.left(90)
        s+=p
        t.pendown()
