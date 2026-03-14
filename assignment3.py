'''str=input("Enter a string: ")
if str==str[::-1]:
    print("palindrome")
else:
    print("Not")'''

'''l1=[1,2,3,4,5,6]
sum=0
for i in l1:
    sum+=i
avg=sum/len(l1)
print(avg)'''

'''l1=[1,2,7]
l2=[2,4,5]
l3=l1+l2
l3.sort()
print(l3)'''

'''info={"Alice":23,
      "Bob":25,
      "Jack":45}
while True:
    op = input("A:Add a student B:Update marks C:Search student D:Display E:Exit")
    if(op == 'A'):
        name,marks = input('enter name and marks').split()
        info.update({name:int(marks)})
    elif(op == 'B'):
        name = input('enter name')
        marks = int(input('enter updated marks'))
        info['name'] = marks
    elif op == 'C':
        name = input('enter name ')
        info.get(name)
    elif op == 'D':
        print(info)
    elif op == 'E':
        break
    else:
        print('invalid input')'''

'''words=["apple","banana","kiwi","cherry","mango"]
dict1={}
for i in words:
    dict1.update({i:len(i)})
print(dict1)'''

'''l1=set([1,2,3,4,5])
l2=([1,7,89])
l3=l1.intersection(l2)
if l3==set():
    print("No common")
else:
    print("Common")'''

'''l1=[1,2,4,2,3,5,7,4]
seen=set()
duplicates=set()
for i in l1:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)
print(duplicates)'''

str=input("Enter a string: ")
unique=set(str)
print(unique,len(unique))
