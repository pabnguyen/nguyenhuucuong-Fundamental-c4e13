menu = ['chan ga', 'Canh ga', 'Dau ga','Duoi ga']
print(*menu,sep = ', ')

print('* '*10)

myguess = input('Nhap mon ban muon xoa: ')
if myguess in menu:
    menu.remove(myguess)
    print(*menu,sep=',')
else:
    print("ko co mon muon xoa")
