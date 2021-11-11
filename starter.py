print('Hello World')

first_name = 'Casper'
last_name = 'Yonel'

age = 23

def newFunc(f, l):
    print(f + ' ' + l)

newFunc(first_name, last_name)

if age == 18:
    print("The age is 18")
elif age > 18:
    print("I am an adult")
else: 
    print("Not an adult")

favorite_numbers = [23, 34, "True", True, 23 ,3 , "hello"]
print(favorite_numbers)

for item in favorite_numbers:
    print(item)

def newFunc2(a, b):
    return(a + b)

print(newFunc2(5, 6))


total_a = 0
total_b = 0
total_c = 0

open_file = open("FinalGrades.csv")
print(open_file)

# for line in open_file:
#     line = line.strip()
#     values = line.split(',')
#     print(values)
#     for value in values: 
#         if value == "A":
#             total_a += 1
#         elif value == "B":
#             total_b += 1
#         elif value == "C":
#             total_c += 1

# print("A's:" , total_a,"B's:" , total_b,"C's:" , total_c)

for line in open_file: 
    line.strip()
    values = line.split(',')
    print(values[0: 2])

    # append or extend adds items to an array
    # [3:] makes it grab the list from 3 to the end
    # [-1: ] is possible too

open_file.close()

prime_number = float(1)
print(prime_number)