def  add(a,b,c):
    print(a+b+c)



add(1121,5,3)  
add(1,51221,3)  
add(1,5,3)  
add(1,1125,3)  
add(1,5,12123)  
add(1121,5,3)  
add(1,5,12123)  


def si(p,t,r):
    value = (p*t*r)/100
    return value

print(si(100,66662,4))
print(si(100888,2,4))
print(si(100,277,4))
print(si(100,2,489797))
print(si(100,27996,4))
print(si(100676,2,4))
print(si(100,289887,4))


def user_info(fname,lname):
    return f' my name is {fname} {lname}'
print(user_info(fname="bijay ",lname='kharel'))





def user_info(fname,lname):
    return f'my name is {fname} {lname}'
print (user_info("bhandari ", "sudan"))




def process_order(item, price, discount=5):
    if discount>100 or discount<0:
        return "invalid argument"
    discount_amount = price*(discount/100)
    final_price = price - discount_amount
    return f'Final price of {item} is {final_price} and received flat {discount_amount} discount'

print(process_order("macbook",450000))
print(process_order(item = "macbook",discount=4, price=10))




def force(a,g=9.8):
    print("the value of g is ",g)

force(2,99)