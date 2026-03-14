
'''with open("names.txt","w") as f:
    names=input("Enter names: ").split()
    for name in names: 
        f.write(name+"\n")

with open("names.txt","r") as f:
    print(f.read())'''

'''with open("logs.txt","a") as f:
    data="Program run successfully"
    f.write(data)

with open ("logs.txt","r") as f:
    print(f.read())'''

'''numbers=[5,10,15,20,25]
new_list=[ i for i in numbers if i>15]
print(new_list)'''

'''import json

d={
    "India":23000,
    "China":35000,
    "Japan":40000
}

with open("cities.json","w") as f:
    json.dump(d,f,indent=4)

with open("cities.json","r") as f:
    data=json.load(f)
    print(data)

city=input("Enter city: ")
pop=int(input("enter population: "))
data[city] = pop

with open("cities.json", "a") as f:
    json.dump(data, f, indent=4)'''

try:
    f=open("data.txt")
except FileNotFoundError:
    print("File not found")
else:
    print(f.read())
    f.close()
finally:
    print("End Of Program")

