from turtle import *

color1 = ['red', 'blue', 'brown', 'yellow', 'grey']

for m in range(5):
    color(color1.pop(0))
    begin_fill()
    for i in range(2):
        fd(50)
        left(90)
        fd(100)
        left(90)
    end_fill()
    fd(50)
mainloop()
