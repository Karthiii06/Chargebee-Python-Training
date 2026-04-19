"""
multiple
lines
commenting
"""
#fundamental datatypes
"""
datatypes
int
float
string
complex
bool
"""
a = 5
b = 1.1
c = "chargebee"
d = 4+2j
e = True
print(a,b,c,d,e)
print(type(a),type(b),type(c),type(d),type(e))

#collection datatypes

list   a = [ item1, item2, ...] 
tuple  b = ( item1, item2, ... )
set    c = { item1, item2, ...}
dict   d = {key:value,key:value,key:value,...}

#string operations

a = "Karthik"
#    0123456
print(a)
print(a[0]) #K
print(a[4]) #h
print(a[-1]) #k
print(a[-3]) #h

#print(a[start index:stop index-1])

print(a[4:6]) #hi

#print(a[start index:stop index-1:step])

print(a[::2]) #alternate
print(a[::-1]) #reverse

b = "Bavani Kandhan"
print(b[9:6:-1]) #naK
print(b[-5:-8:-1]) #naK
print(b[9:-8:-1]) #naK
print(b[-5:6:-1]) #naK

b = "    Manideep Thalluru    "
print(b.strip())
print(b.lstrip())
print(b.rstrip())


a = ["usha", "manideep", "abirami"]
print(a)
print(type(a))

b = ("usha", "manideep", "abirami")
print(b)
print(type(b))

a[0] = "Baradwaj"
print(a)

#b[0] = "Baradwaj"

c = {1,1.1,"i"}
print(c)

d= {1:"ravi", 2:"raj"}
print(d)
print(d[1])

"""
print a dict give key as vegetables, fruits... also it should say each
type of friut name and count. hint: dict inside dict
"""

d= {"veg":{"tamato":5,"brinjal":10}, "fruits":{"apple":5,"banana":10}}
print(d)
print(d["veg"])

#conditional statments

if, elif, else

#loops

for, while

password= "admin@123"
limit =0
while (limit<3):
    entry = input("Enter the password")
    if (password == entry):
        print("password match")
        break
    else:
        print("check your password")
        limit = limit+1
else:
    print("attempt limit reached")
