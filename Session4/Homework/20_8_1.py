while True:
    my_data = input("Enter data: ").lower()
    #0. Sắp xếp
    l = list(my_data)
    l.sort()
    lettercount = {}
    #1. Thêm phần tử vào lettercount
    for letter in l:
        lettercount[letter] = lettercount.get(letter, 0) + 1
    #2. In ra
    for k in lettercount.keys():
        if k == " ":
            continue
        else:
            print(k,lettercount[k])
    my_choice = input("You want to cotinue Y/N? ").lower()
    if my_choice == 'n':
        break
