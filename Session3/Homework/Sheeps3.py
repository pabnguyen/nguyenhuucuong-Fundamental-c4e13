
#2.6

mySheeps = [5,7,300,90,24,50,75]
print("My name is Hiep and these are my sheep sizes")
print(*mySheeps,sep = ',')

months = int(input("Enter Your Months: "))
for i in range(0,months+1):
    if i != 0:
        print("MONTH",i)
        print("one month has passed: ")
        for j in range(len(mySheeps)):
            mySheeps[j]+=50
        print(*mySheeps,sep =",")
    if i == months:
        s = sum(mySheeps)
        print("My flock has size in total",s)
        print("I would get ",s*2,"$")
        break
    max = mySheeps[0]
    for u in range(len(mySheeps)):
        if max < mySheeps[u]:
            max = mySheeps[u]
            save = u
    print("My biggest Sheep is size",max,"Let's Shear it")
    mySheeps[save] = 8
    print("After Shearing:")
    print(*mySheeps,sep = ',')
#end
