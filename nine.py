
name="bijaykharel"
letter="a"
letter_position=0
for i in name:
    letter_position=letter_position  +1
    if (i==letter):
        print("Letter found in ", letter_position)
        break
print(letter_position)


i = 1
while (i <= 10):
    print("hello")
    i = i + 1



    
random_num = 77
guess_time = 0
while True:
    num = int(input("enter a number "))
    guess_time = guess_time + 1
    if num==random_num:
        print(f'number match in  {guess_time} time')
        break

   
