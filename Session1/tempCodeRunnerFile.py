yob = int(input("Your year of birth? "))
print("Hello",yob)
age = 2017 - yob
print(age)
if age < 10:
    print("Baby")
elif age < 18:# có 3 con đường chỉ chọn 1 và ko chọn cái còn lại
    print("Teenager")
else:
    print("adult")
print("Bye Bye")
