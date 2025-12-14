age = int(input("Enter your age: "))

license = input("Do you have a driving license? (yes/no): ")
vehicle = input("Do you have your own vehicle? (yes/no): ")
if age >= 18:
    if license == "yes":
        if vehicle == "yes":
            print("You can drive alone.")
        else:
            print("You have a license but no vehicle.")
    else:
        print("You must get a driving license first.")
else:
    if age >= 16:
        print("You can only drive with supervision.")
    else:
        print("You are not allowed to drive.")




 
                   

