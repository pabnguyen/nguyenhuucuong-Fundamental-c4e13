from random import choice
#1.Tạo ra chuỗi
s = 'Halloween'
l = []
characters = list(s)
m = len(characters)

#2.Bắt đầu tiến hành chuyển các phần tử từ characters sang l
i = 0
while m <= len(characters) and m > 0:
    c = choice(characters) #lấy một phần tử ngẫu nhiên trong characters
    l.insert(i,c) #chèn c vào vị trí i
    characters.remove(c) #xóa phần tử c
    m -= 1 #giảm độ dài list xuống
    i += 1 #chèn vào vị trí i+1 trong vòng lặp tiếp

print(*l,sep = ',')

#3.Cho người dùng nhập và in ra kết quả
MyOpinion = input("Enter Your String ")
if MyOpinion == s:
    print("Bingo")
else:
    print("Wrong")
