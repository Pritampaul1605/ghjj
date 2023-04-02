#2. Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.

list = []
while (True) :
    p = int(input('Enter number :'))
    list.append(p)
    n = input("if you want to stop press y. otherwise press any key")
    if(n == 'y') :
        break
count = 0
for i in list :
    count = count + 1
print("The length of the list is :",count)
a = list[4]
print("The fifth element of the list is ",a)
b = 0
for i in list :
    if(i == a) :
        b = b+1
if(count == 8) & (b == 3) :
    print('True')
else : print('False')
