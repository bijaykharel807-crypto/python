def add(*a):
    print("inside func")


add(1,2)
add(1,2,3)    
add(1,2,3,4,5,4)


def add(*sudan):
    print(sudan)
    print("inside func")


add(1,2)
add(1,2,3)    
add(1,2,3,4,5,4)


def add(data,*sudan):
    print(sudan)
    print(data)


add(1,2)
add(1,2,3)    
add(1,2,3,4,5,4)



def progress_report(name, *marks):
    sum = 0
    len_marks = len(marks)
    for i in marks:
        sum = sum + i
    
    return f'{name} percentage is {sum/len_marks} where total subject is {len_marks}'

print(progress_report("Sudan", 85, 90, 78))






