a=[1,1,2,3,4,"hello",5,6,7, True,.1]
print(type(a))
print(a[4]) 
print(len(a))
print(a[10],a[-11])


print(a[5:9])

data=['hello','hi']
data.append('Namaste')
print(data)




data2=["Sudan", "Ramesh","Hari"]
data2.insert(1,"bhandari")
print(data2)

data1=[1,2,3]
data3=[4,5,6]
data3.extend(data1)
print(data3)

a=[1,2]
b=["hello","hi"]
c=a+b
print(c)



marks=[]

eng =int(input("Enter a marks"))
math =int(input("Enter a marks"))
marks.append(eng)
marks.append(math)
total=marks[0]+marks[1]
Percentage = total/2

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

