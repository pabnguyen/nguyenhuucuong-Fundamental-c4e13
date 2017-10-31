#refctor: tối ưu code
a = int(input("Nhập a "))
b = int(input("Nhap b "))
c = int(input("Nhap c "))
# 2*a và delta**0.5 sử dụng nhiều lần đặt vào biến
if a == 0:
    x3=-c/b
    print("co nghiem ",x3)
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        #chia thanh ba tap hop rieng biet,khi da thoa man if nay thi se ko xet cac if khac
        print("Phuong trình vo nghiem")
    elif delta == 0:
        print("Phuong trinh co nghiem kep", x = (-b/(2*a)))
    else:
        x1 = (-b+delta**(1/2))/(2*a)
        x2 = (-b-delta**(1/2))/(2*a)
        #print("Phu trinh co 2 nghiem x1 = ",x1, "x2 = ",x2)
        print("2 nghiem: x1={0}, x2={1}".format(x1, x2)) #được gọi là chỗ trống chờ lấp đầy
        # print(x1)
        # print(x2)
