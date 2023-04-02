#6. Write a Python program to test a list of one hundred integers between 0 and 999, which all differ by ten from one another. Return True otherwise False

list = []
print("please enter 100 integers")
for i in range(10) :
    n = int(input(f'Enter {i} integer :'))
    list.append(n)
print(list)
flag = 1
for i in range(9) :
    if((list[i+1] - list[i]) != 10) :
        flag = -1
        break
if(flag == 1) : print("True")
else : print('False')
