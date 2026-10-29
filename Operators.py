# arthematic operators

a = int(input("enter the value of a = "))
b = int(input("Enter the value of b = "))

#Arthematic operators
print("Arthematic operators")
print("a+b = " , a+b)
print("a-b = " , a-b)
print("a/b = " , a/b)
print("a*b = " , a*b)
print("a%b = " , a%b)

#relational operator
print("relational operator")
print("a==b = ", a==b)
print("a!=b = ", a!=b)
print("a>b  = ",  a>b )
print("a>=b = ", a>=b)
print("a<b  = ",  a<b )
print("a<=b = ", a<=b)

#Assignment operator
print("Assignment operator")
c = 10
c +=10
print("c+=10  : " , c)
c -=5
print("c-= 5  : " , c)
c *=2
print("c*=2   : " , c)
c /=2
print("c/=2   : " , c)

#Logical Operator
print("Logical operator")
e = True
f = False
print(e and f )
print(e or f)
print(not f)

#Bit-Wise operator
print("Bit-Wise operator")
g = int(input("Enter the value of the g = "))
h = int(input("Enter the value of the h = "))

print("g&h  : " ,g&h)
print("g/h  : " ,g/h)
print(" ~h  : " , ~h)
print("g<<h : ",g<<h)
print("g>>h : ",g>>h)
