n = int(input("Enter your number: "))
print("C1")
for i in range (0,n,2):
    print(i,end = " ")
#print(*range(n))
print("\nC2")
for i in range (n):
    if i%2 == 0:
        print(i,end = " ")
