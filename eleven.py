a = (1,2,3,4,5,6,7)
print(type(a))


data=list(a)
data.remove(5)
print(tuple(data))



a = {1,"test",2,2,1,2,"hello"}
a = [1,"test",2,2,1,2,"hello"]
c = set(a)
print(c)




for i in a:
    print(i)

''''''
#  def function_name():
#      <code block>
#       return <any thing>


''''''''
def sudan():
    a = 10
    b = 11
    print(a)
    return a,b
print(sudan())

def sudan():
    a = 10
    b = 11
    print(a)
    return a+b
print(sudan())




def sudan():
    a = 10
    b = 11
    print(a)
    return a,b


data = sudan()
add = data[0] +data[1]
print(add)



def sudan():
    sum=0
    for i in [1,2,3,4,54,5,6,7,7]:
        sum = sum+i

    return sum
data = sudan()
print(data)


def  sudan():
    a = 10
    b = 11
    return a+b
data = sudan()
print(data)

