#if else condition

age = int(input("enter the age of the person = "))

if age>18 and age<150 :
    print("The person is eligible for the vote")
elif age<0:
    print("The person age is invalid")
else :
    print("The person is not eligible for voting")

#login password

person = input("Are u an admin or user :")

if person in ("ADMIN","Admin","admin"):
     password = input("Enter the password :")
     if password == "123abc"or"123ABC":
         print("login confirmed!...")
     else :
         print("you have entered an wrong password")
elif person in ("USER","User","user"):
     password = input("Enter the password :")
     if password == "user123"or"User123"or"USER123":
         print("login confirmed!...")
else :
    print("specify the person ur logging correctly")

#converting meters to kilometers

dist = float(input(("Enter the distance : ")))
measure =  input("enter weather u entered in m or km or mil : ")
conv = input("in what parameter u want to change the distance : ")

if measure == "m"and conv == "km" :
    dist = dist/1000
    print(f"The distance in the km = {dist}km")
elif measure == "m"and conv == "mil":
    dist = dist*0.621371
    print(f"The distance in the mil = {dist}mil ")
elif measure == "km"and conv == "m":
    dist = dist*1000
    print(f"the distance in the m = {dist}m")
elif measure == "km" and conv == "mil":
    dist = dist*0.621371
    print(f"the distance in the mil = {dist}mil")
