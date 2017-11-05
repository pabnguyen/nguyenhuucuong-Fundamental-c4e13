from turtle import *


color = ['red', 'blue', 'brown', 'yellow', 'grey']
m = 5
for n in range(3,m+3):
    for i in range(n):
        myColor = n - 3
        pencolor(color[myColor])
        fd(100)
        left(360/n)


mainloop()
