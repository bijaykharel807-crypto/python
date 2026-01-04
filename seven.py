'''
for <variable>  in <multiple data>
<variable> 
'''
for i in [1,2,3,4,5,6,7]:
    print(i+i)
    print(f'{i} loop')
    if i==4:
        print("its 4")
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                if ( i%2== 0):

                    print(f"{i} is even")
                else:
                    print(f"{i} is odd")


odd =[]
even =[]

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if (i % 2 == 0):
        even.append(i)
        
    else:
        odd.append(i)
        even.sort()
        odd.sort()
        print(even,'Even')
        print(odd,'ODD')
for i in "sudan":
    print(i)
for i in range(20,51,1):
    print(i)
for i in range(51):
    print(i)
for i in range(2,10,1):
    if i%2==0:
        print(i,"even")
        
for i  in range(10,-1,-1):
      print(i)
for i in range(10,-1,-1):
      if i==7:
            break
      print(i)
for i in range(10,-1,-1):
    if i==7:
        continue
    print(i)



student = {"name" : "hari",  "age" : 16 }
for i in student :
    print(i)
for i ,values in student .items ():
    print(i,":", values)  
     

















