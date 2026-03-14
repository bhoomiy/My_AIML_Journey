'''a=float(input("Enter a floating number: "))
print("The integer part is: ",int(a),"and decimal part is: ",round(a-int(a),2))
'''

a=int(input("Enter a number: "))
i=1
while i<=10:
    print(f'{a}x{i}={i*a}')
    i+=1

