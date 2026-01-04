class Car():
    wheel=4


data=Car()
print(data)


class Car():
    wheel=4


data=Car()
print(data.wheel)

class Math():
    a=10
    b=11


    def add(self):
        return self.a+self.b
    

obj =Math() 
print(obj.add())   




def fibbo(n):
     if n==1 or n==0:
         return 1
     else:
              return n * fibbo(n-1) 
         
print (fibbo(5))


def fibbo(n=5):
     if n==1 or n==0:
          return 1
     else:
          return n *fibbo(n-1)
print(fibbo(10))    


def test(sudan,bhandari):
     a=sudan
     b=bhandari
     return a+b
data = test(bhandari=1,sudan=111)
print(data)
data = test(1,2)
data = test(1,4)
data = test(1,1)





print(data)

class Car():
     wheel=4

def test():
     pass
def tet2():
     test()



class Car():
    wheel=4


data=Car()
print(data.wheel)   

data1= Car()
data1.door = 10
print(data1.door)



data = Car()
print(data .wheel)


print(data.wheel)
del data






