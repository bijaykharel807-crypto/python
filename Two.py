
Percentage = (input("Enter your percentage"))
if(Percentage.isalpha()):
    print('Percentage is alpha')
if int(Percentage)>100 or int (Percentage)<0:
    print("invalid")
elif int(Percentage)<=100 and int(Percentage) >=80:
    print("Distinction")
elif int(Percentage)<80 and int(Percentage)>=70:
    print("First Division")
elif int(Percentage)<70 and int(Percentage)>=60:
    print("Second Division")
elif int(Percentage)<60 and int(Percentage)>=50:
    print("Third Division")
else:
    print("fail")






















 
    