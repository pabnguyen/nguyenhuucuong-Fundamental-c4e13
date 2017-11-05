#2.1. create myList of Sheeps
mySheeps = [5,7,300,90,24,50,75]
print("My name is Hiep and these are my sheep sizes")
print(*mySheeps,sep = ',')

#2.2. Search for biggest size
# mySheeps.sort()
# m  = mySheeps.pop()
# print("My biggest Sheep is size",m,"Let's Shear it")
maxSheep = max(mySheeps)
print("My biggest Sheep is size",maxSheep,"Let's Shear it")

#2.3. After Shearing
Sheared = 8;
mySheeps[2] = Sheared
print("After Shearing,here is my flock: ")
print(*mySheeps,sep = ',')

#2.4. Following month
print("one month has passed: ")
for j in range (len(mySheeps)):
    mySheeps[j]+=50
print(*mySheeps)

print("*"*40)
#2.5 in Sheeps2.py
