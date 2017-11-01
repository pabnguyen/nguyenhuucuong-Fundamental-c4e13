from turtle import *
color('red')
for i in range(4):
    if i == 2:
        left(120)
    else:
        left(60)
    fd(100)
left(60)

for i in range (4):
    if i == 0:
        left(30)
    elif i == 2:
        right(120)
    else:
        right(60)
    fd(100)
left(30)

for i in range (4):
    if i == 0:
        right(30)
    elif i == 2:
        left(120)
    else:
        left(60)
    fd(100)
right(120)

for i in range (4):
    if i == 0:
        right(30)
    elif i == 2:
        left(120)
    else:
        left(60)
    fd(100)

mainloop()
