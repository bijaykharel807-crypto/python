
Percentage = (input("Enter your percentage"))
if(Percentage.isalpha()):
    print('Percentage is alpha')
if int(Percentage)>100 or int (Percentage)<0:
    print("invalid")
elif int(Percentage)<=100 and int(Percentage) >=80:
    print("Distinction")
elif(Percentage<80 and Percentage>=70):
    print("First Division")
elif(Percentage<70 and Percentage>=60):
    print("Second Division")
elif((Percentage<60 and Percentage>=50)):
    print("Third Division")
else:
    print("fail")






















 
    