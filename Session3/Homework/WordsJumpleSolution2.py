from random import choice

#1.Tạo ra chuỗi
s = 'CodeTheChange'
characters = list(s)
m = len(characters)

#2.In ra chuỗi đã sắp xếp random
i = 0
while i>=0 and i < m:
     c = choice(characters)
     characters.insert(i,c)
     characters.remove(c)
     i+=1
print(*characters,sep = ',')

#3.Cho người dùng nhập và in ra kết quả
MyOpinion = input("Enter Your String ")
if MyOpinion == s:
    print("Bingo")
else:
    print("Wrong")
