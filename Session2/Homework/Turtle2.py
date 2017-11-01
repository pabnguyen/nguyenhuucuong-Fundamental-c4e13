from turtle import *

color("blue")

for i in range(3):#Vẽ tam giac
    fd(100)
    left(120)
fd(100)

for i in range(5):#Vẽ ngũ giác nhỏ
    left(72)
    fd(100)
    
color('red')#đổi màu

for i in range (4):#Vẽ Hình Vuông
    left(90)
    fd(100)


for i in range(5):#Vẽ ngũ giác to
    left(60)
    fd(100)


mainloop()
