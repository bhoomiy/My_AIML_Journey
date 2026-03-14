'''sal=int(input("Enter your salary: "))
if sal<30000:
    tax=(sal*5)/100
if sal>=30000 and sal<70000:
    tax=(sal*15)/100
if sal>70000:
    tax=(sal*25)/100
print("Your tax value is: ",round(tax,2))'''

'''a=int(input("Enter number: "))
b=int(input("Enter number: "))
for i in range(a,b+1):
    if i%2==0:
        print(i)'''

'''n=int(input("Enter a number: "))
sum=0
for i in str(n):
    sum+=int(i)
print(sum)'''

'''while True:
    n=int(input("Enter a number: "))
    if (n<0):
        print("Negative")
    else:
        print("Positive")
    choice=input("Continue?(Y/N): ")
    if choice=="break" or choice=="N" or choice=="n":
        break'''

'''def calculator(a,b,opr):
    match(opr):
        case "+": 
            return a+b
        case "-": 
            return a-b
        case "*": 
            return a*b
        case "/":
            if b==0:
                print("Division not possible")
                return 0 
            return a/b

print(calculator(3,5,"+"))'''

'''def is_prime(n):
    for i in range(2,n-1):
        if n%i==0:
            return False
    return True
    
print(is_prime(9))'''

num=int(input("Enter a number: "))
ans=23
if num>ans:
    print("Guess too high")
elif num==ans:
    print("Correct")
else:
    print("Guess low")