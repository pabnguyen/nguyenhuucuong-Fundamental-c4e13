menu = ['death note','netflix','teaching']

for index, item in enumerate (menu):
    print(index + 1,'.',item,sep = '')
m = int(input('enter your position '))
m-=1
n = input("Enter yours: ")
menu[m] = n
for index, item in enumerate (menu):
    print(index+1,'.',item,sep = '')
