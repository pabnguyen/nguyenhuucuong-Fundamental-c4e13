px = 4
py = 3

for i in range (10):
    for j in range(10):
        if i == px and j == py:
            print("P ",end = "")#Thông báo cho người chơi
        else:
            print("* ",end = "")
    print()
