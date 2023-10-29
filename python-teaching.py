# marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]
# print(marks)
# # type is used to check data type of variable
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])


# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index

# if "6" in marks:
#   print("Yes")
# else:
#   print("No")

# Same thing applies for strings as well!
# if "Ha" in "Harry":
#   print("Yes")

# print(marks[0:7])
# print(marks[1:9])
# print(marks[1:9:3])

# lst = [i*i for i in range(10)]
# print(lst)

# j=1
# lst = [j for i in range(10) if i%2==0]
# print(lst)

#############################################


# l = [11, 45, 1, 2, 4, 6, 1, 1]

# l.sort()
# print(l)

# print(dir(list))

# print(l)
# l.append(7)
# l.sort(reverse=True)
# l.reverse()
# print(l.index(1))
# print(l.count(1))
# m = l.copy()
# m[0] = 0
# l.insert(1, 899)
# m = [900, 1000, 1100]
# k = l + m
# print(k)
# l.extend(m)
# print(l)

# def is_even_or_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# user = int(input("Enter any number: "))
# result = is_even_or_odd(user)

# print(result)

# import time

# hours = int(time.strftime("%H"))
# hours = int(input("Enter hours: "))

# for i in range(1,11):
# print(i)

# print(hours)

# if (hours > 0 and hours < 4) or (hours >= 20):
#     print("Good Night")
# elif (hours >= 4 and hours < 12):
#     print("Good Morning")
# elif (hours >= 12 and hours < 16):
#     print("Good Afternoon")
# elif (hours >= 16 and hours < 20):
#     print("Good Evening")


# def myFunc(a, b):
#     return a+b

# result = myFunc(5,6)
# print(result)


# list, tuple, set, dict


# List

# lst = [1, 2, 6, 9, 1, 50, 5]
# str = "Hello"

# if "ello" in str:
#     print("yes")

# else:
#     print("No")

# s = {1, 5, 2, 2, 5}

# s.update("Hell")
# print(s)

# print(lst[1])
# print(lst[-1])
# print(type(lst))
# print(len(lst))
# print(lst[start: end: jumpindex])
# print(lst[::])
# print(str[:4:2])
# lst.append("Hi")
# lst.sort(reverse=True)
# lst.remove()
# print(lst.pop(2))
# print(lst.count(1))
# lst.insert(1, 10)
# lst2 = lst.copy()
# lst2[0] = 20
# print(dir(list))

# print(lst)


# tuple

# mutable, immutable

# tuple1 = (1, 5, 3, 4, 6)
# lst = list(tuple1)
# lst[0] = 6
# tuple1 = tuple(lst)
# print(tuple1)
# tuple[0] = 5
# print(type(tuple))
# print(type(tuple))

# dev = [1,33,43,55,87,"devanshi","anshi","vanshi"]
# if "ashu" in dev:
#     print("yes")
# else:
#     print("no")

# dev[8]=45
# to add new emement in last append....insert after index
# dev.append(33)
# dev.insert(1,34)
# print(dev)

# a = 12345
# s = str(a)
# # deva="hello"
# print( [::-1])
# print(deva)

# l = [22, 33, 44, "hello",11,22,33]
# m = [1, 2, 3]
# m=l
# m[0]=10
# print(m)
# print(l)

# m=l.copy()
# m[0]=10
# print(l)
# print(m)

# a=l+m
# print(a)

# l = l+m
# lst = [22, 33, 44,11,22,33]
# lst.sort()
# print(lst)


# dic = {"name": "Karan", "age": 16}

# for key in dic:
#     print(f"The {key} of employee is {dic[key]}")

# for key, val in dic.items():
#     print(f"The {key} of employee is {val}")


# try:
# num = int(input("Enter an integer: "))
# if num < 0:
#     raise Exception("Enter number greater than 0")
# a = [6, 3, 5]
# print(a[num])
# except:
# except ValueError:
#     print("Number entered is not an integer.")
# except IndexError:
#     print("Invalid index")
# finally:
#     print("The statement is executed")

# def myFunc():
#     try:
#         num = int(input("Enter an integer: "))
#         return num
#     except:
#         print("Invalid input")
#     finally:
#         print("This statement will get executed")

# result = myFunc()
# print(result)


# class Person:
#     name = "Krishna"
#     occupation = "Web Developer"
#     salary = 50000

#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

# a = Person()
# b = Person()

# a.name = "Karan"
# a.info()

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   pass

# x = Student("Mike", "Olsen")
# x.printname()

# print(x.firstname)




# import os

# if not os.path.exists("KK/New folder/data"):
#   os.mkdir("KK/New folder/data")

# for i in range(0, 100):
#   os.mkdir(f"KK/New folder/data/{i+1}")

# for i in range(0, 100):
#   os.rename(f"KK/New folder/data/{i+1}",f"KK/New folder/data/folder{i+1}")



# f = open("KK/on.png", 'rb');
# f = open("KK/myFile.txt", 'w');

# # text = f.read()
# text = f.write("Hello world")
# print(text)

# f.close()

