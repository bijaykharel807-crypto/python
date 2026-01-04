from module_143 import *
print(progress_report("hari", 50))

from module_Six import *
print(teachers)


eng = int(input("enter a eng marks"))
nep = int(input("enter a nep marks"))
math = int(input("enter a math marks"))
name = input("enter a namr")

print(progress_report(name,eng,nep,math))


def test(**kwargs):
    print(type(kwargs))
test(name="bijay", address="dang") 

def testing(*args,**kwargs):
    print(args)
    print(kwargs)

testing(1,"sydddd",1,1,1,1,1, name="testing",hello="greeting")