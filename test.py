experience=int(input("enter experience"))
performance_rating=int(input("enter performance rating"))
attendance_rating=int(input("enter attendance rating"))


experience = 5
rating = 5.5
attendance = 95

if experience >= 5:
    if rating >= 4.5:
        if attendance >= 95:
            print("Your experience is",experience,"years", "rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is Platinum")
        elif attendance >= 85:
            print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is Gold")
        else:
            print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is Silver")
    elif rating >= 3.5:
        if attendance >= 90:
            print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is Silver")
        else:
            print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is Bronze")
    else:
        print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is No Bonus")
        
elif experience >= 2:
    if rating >= 4:
        print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is Silver")
    elif rating >= 3:
        print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is Bronze")
    else:
        print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is No Bonus")
else:
    print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","You are not eligible") 
    