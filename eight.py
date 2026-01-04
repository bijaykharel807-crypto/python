a=[1,2,3,4,5,6,7,8,9,"sudan",90 ,"hari","adad","aadsakj"]
for i in a:
    if isinstance(i,int):
        continue
    print(i)
for i in [1,2,3]:
    for j in [4,5,6]:
        print(i,j)

random_num=77
guess_time=0
num2 = int(input("Enter num2 for guess time"))
for i in range(0,num2,1):
    num=int(input("enter a number"))
    guess_time= guess_time +1
    if num==random_num:
        print(f'number match in {guess_time} time')
        break
else:
    if guess_time <=5:
        print("random number was", random_num)



name="bijaykharel"
letter="a"
letter_position=0
for i in name:
    letter_position=letter_position  +1
    if (i==letter):
        print("Letter found in ", letter_position)
        break
      



