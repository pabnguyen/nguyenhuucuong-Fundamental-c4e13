#1. List có nhiều từ
#2. random -> ra word
#3. word -> '------'
#4. guess -> 'đúng hay sai' l = list(word)
#5. 'vodka' -> " _ _ _ _ _ a" enumrate
#6. thắng thua
statues = [
"""
|------
|     o
|     |
|
|
"""
,
"""
|------
|     o
|     |-
|
|
"""
,
"""
|------
|     o
|    -|-
|
|
"""
,
"""
|------
|     o
|    -|-
|      \\
|
"""
,
"""
|------
|     o
|    -|-
|    / \\
|
"""
,
]
import random

mylist = ['apple', 'banana','orange']


solution = random.choice(mylist)
list_solution = list(solution)
print("_ "*len(list_solution),sep = " ")

#4 guess
mylist1 = []
for i in range (len(list_solution)):
    mylist1.insert(i, '_')
count = 0
count1 = 0
a = True
while a:
<<<<<<< HEAD
    your_guess = input("Your word? ").lower();
=======
    your_guess = input("Your word? ").lower()
>>>>>>> a899931a0c52fe71f36b1a45b0e2cf20f46081f9
    if your_guess in list_solution:
        if your_guess in mylist1:
            print("You Guessed")
            continue
<<<<<<< HEAD
        print("You Right!")
=======
        print("You Right!")      
>>>>>>> a899931a0c52fe71f36b1a45b0e2cf20f46081f9
        for index, item in enumerate(list_solution):
            if list_solution[index] == your_guess:
                mylist1[index] = your_guess
                count1 +=1

        print(*mylist1,sep = " ")
        if count1 == len(list_solution):
<<<<<<< HEAD
            print("You Win")
            break
    else:
        print("You Wrong")
=======
            print("You are WINNER!")
            break
    else:
        print("You Were Wrong")
>>>>>>> a899931a0c52fe71f36b1a45b0e2cf20f46081f9
        count += 1
        if count == 1:
            print(statues[0])
        elif count == 2:
            print(statues[1])
        elif count == 3:
            print(statues[2])
        elif count == 4:
            print(statues[3])
        else:
            print(statues[4])
<<<<<<< HEAD
            print("you lose")
=======
            print("YOU ARE LOSER")
>>>>>>> a899931a0c52fe71f36b1a45b0e2cf20f46081f9
            a = False
