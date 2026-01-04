import random


random_item = [1,2,3] 
mapping_item = {
    "1":"Scissor",
    "2":"Rock",
    "3":"Paper"
}

while True:
    com_selected = random.choice(random_item)
    print(com_selected)
    user = int(input("Enter 1: for scissor and 2: for rock and 3: for paper "))
    if user == com_selected:
        print("its draw")
    elif(
        (user==1 and com_selected==3) or
        (user==2 and com_selected==1 ) or
        (user==3 and com_selected==2)
    ):
        print(f'User choice is {mapping_item.get(str(user))} and computer choice is {mapping_item.get(str(com_selected))} so user win' )
    else:
        print(f'User choice is {mapping_item.get(str(user))} and computer choice is {mapping_item.get(str(com_selected))} so computer win' )

    play_again = input("Do you want to play again y/n").lower()
    if play_again == "y":
        print("Lets play again")
    else:
        break




import random

random_num = random.randint(1, 30)
print(random_num)  

guess_time = 0
while True:
    num = int(input("enter a number "))
    guess_time = guess_time + 1
    if num == random_num:
        print(f'number match in {guess_time} time')
        break
    


