from turtle import *

shape("turtle")
speed(-1)
for i in range (200):
    forward(100)
    left(90)
    if i % 4 == 0 and i > 2 :
        left(7)
mainloop()
