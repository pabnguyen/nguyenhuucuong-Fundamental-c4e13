teen_dicti = {

    'rh' : 'Rảnh rỗi',
    'cn'  : 'con',
    'kcj' : 'Không có gì',
    'ps' : 'tái bút',
    'kqt' : 'Không Quan Tâm',
    'wtf' : 'Cái đ*o gì vậy',
    'r' : 'ròi',

}
while True:
    print(*teen_dicti)
    your_code = input("Your Code? ")
    if your_code in teen_dicti:
        print(teen_dicti[your_code])
    else:
        your_choice= input("You want to update it (y/n)?").upper();
        if your_choice.upper() == 'Y':
            your_add = input("Your Data?")
            teen_dicti[your_code] = your_add
            print(teen_dicti)
        else:
            break
