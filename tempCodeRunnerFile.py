
dist = float(input(("Enter the distance : ")))
measure =  input("enter weather u entered in m or km or mil : ")
conv = input("in what parameter u want to change the distance : ")

if measure == "m"and conv == "km" :
    dist = dist/1000
    print(f"The distance in the km = {dist}km")
elif measure == "m"and conv == "mil":
    dist = dist*0.000621371
    print(f"The distance in the mil = {dist}mil ")
elif measure == "km"and conv == "m":
    dist = dist*1000
    print(f"the distance in the m = {dist}m")
elif measure == "km" and conv == "mil":
    dist = dist*0.621371
    print(f"the distance in the mil = {dist}mil")
elif measure == "mil" and conv == "km":
    dist = dist/0.621371
    print(f"The distance in the km = {dist}km ")
elif measure == "mil" and conv == "m":
    dist = dist/0.000621371
    print(f"the distance in the m = {dist}m")
else :
    print("Enter the specify parameter")
