list = []
a = int(input("Enter the length of the list you want : "))
for i in range(a) :
    list.append(str(input(f"Enter string number {i+1} : ")))
print(list)
new_string = 'b'
for i in list :
    len_1 = len(new_string)
    len_2 = len(i)
    if(len_1 < len_2) :
        new_string = i
print("longest string : ",new_string)