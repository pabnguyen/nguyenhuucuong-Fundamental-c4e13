username = input("Nhap username: ")

while True:
    if username.upper() == 'C4E' : #convert tất cả mà người nhập sang in hoa sẽ phải check 1 lần thôi
#ignoCase ko phân bietj chữ hoa chữ thường
        password  = input("Nhap password:")
        if password == 'codethechange':
            print("xin chao c4e")
        else:
            print("Incorrect")
    else:
        print('user not found')
#IndentationError: unexpected indent la loi dau cach
