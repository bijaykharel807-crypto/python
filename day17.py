class A():
    a=10
    b=11
class B(A):
    a=123
    c=567
obj = B()
print(obj.a)    

class A():
    a=10
    b=11
class B(A):
    d=123
    c=567
obj = B()
print(obj.a)  



class BankAccount():
    acc_Number=12345
    balancae=1221


class SavingAccount(BankAccount):
    interest_rate = 10



    def calc_interest(self):
        interest = (self.balancae * 1 * self.interest_rate)/100


obj = SavingAccount()
print(obj.calc_interest())     



class BankAccount():
    acc_Number="Sudan Bhandari"
    balancae=1221


class SavingAccount(BankAccount):

    def __init__(self,interest_rate):
        self.interest_rate = interest_rate

    def calc_interest(self):
        interest = (self.balancae * 1 * self.interest_rate)/100
        return interest
    

    
obj = SavingAccount(10)
print(obj.calc_interest())  





class BankAccount():

    def __init__(self, account_name, balance):
        print("init form bank")

        self.acc_name = account_name
        self.balance = balance


class SavingAccount(BankAccount):

    def __init__(self, account_name , balance,interest_rate):
        print("init form saving")
        self.interest_rate = interest_rate
        
        super().__init__(account_name, balance)
        return

    def calc_interest(self):
        interest = (self.balance * 1 * self.interest_rate)/100
        return int


obj = SavingAccount("sudan",200,10)
print(obj.calc_interest())
      













   
    

     


      


  



   




    


