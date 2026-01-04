numbers = [10, 20, 30, 40, 50]

print(numbers[0:3])   # [10, 20, 30]  # start 10 end 30 samma ho sab include hunxa
print(numbers[2:5])   # [30, 40, 50]
print(numbers[:2])    # [10, 20]
print(numbers[3:])      # [40, 50]


teachers = ["Ram", "Sita", "Hari", "Gita", "Mohan", "Rita", "Anil", "Puja", "Nabin"]  # hari dakhi 2 count add all included

print(teachers[2:9:2])


nums = [10, 20, 30, 40, 50]

print(nums[-5:-2])   # [10, 20, 30]  # 10 dakhi 40 samma 40 count hudaena
print(nums[-3:])     # [30, 40, 50]
print(nums[:-1])     # [10, 20, 30, 40]



a = [1, 2, 3]
b = [4, 5]

c = a + b
print(c)
print(a)


teachers = ["Ali", "Ahmed", "Haris", "Sheraz"]   #pop

removed = teachers.pop(1)

print(removed)
print(teachers)