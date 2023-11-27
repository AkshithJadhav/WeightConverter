Weight=int(input("Enter Your Weight- "))
x=input("(L)bs or (K)g- ")
if x.upper() =='L':
    Weight*=0.45
    print(f"You are {Weight} Kgs")
elif x.upper() =='K':
    Weight/=0.45
    print(f"You are {Weight} lbs")
else:
    print("Give a valid input!")
 