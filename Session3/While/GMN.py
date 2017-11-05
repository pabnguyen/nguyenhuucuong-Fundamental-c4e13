from random import randrange

m = randrange(1,101)
while True:
    n = int(input("Enter yuor number: "))
    if n < m :
        print("too small")
    elif n >m:
        print("Too large")
    else:
        print("bingo")
        break
print("Winner")
