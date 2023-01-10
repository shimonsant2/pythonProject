# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import json
import os
import random
import re
import camelcase
import np as np
import numpy

import mymodule


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    print_hi('PyCharm')
    print("Hello, World11111!")
    # Example on inputs
    x = 5
    y = "John"
    print(f'x + {y} + {x}')

    # a Python object (dict):
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    # convert into JSON:
    y = json.dumps(x)

    # the result is a JSON string:
    print(y)

    # parse y:
    m = json.loads(y)
    print(m["name"] + " from " + m["city"] + " age : " + str(m["age"]))
    print("Random 1 to 10 -->  " + str(random.randrange(1, 10)))

    print("So Good")

    # RegEx Functions Search the string to see if it starts with "The" and ends with "Spain"
    txt = "The rain in Spain"
    x = re.search("^The.*Spain$", txt)
    if x:
        print("YES! We have a match!")
    else:
        print("No match")

    print("So Good")

    # example how to install package
    c = camelcase.CamelCase()
    txt = "lorem ipsum dolor sit amet"
    txt2 = c.hump(txt)
    print(c.hump(txt))
    print("So Good")

    thislist1 = ["apple", "banana", "cherry", "abba"]
    thislist1.sort()
    for x in thislist1:
        print(x)

    set1 = {"a", "b", "c"}
    set2 = {1, 2, 3}
    set1.update(set2)
    print(set1)

    thistuple = ("apple", "banana", "cherry")
    i = 0
    while i < len(thistuple):
        print(thistuple[i])
        i = i + 1

    thisdict = {
        "brand": "Ford",
        "electric": False,
        "year": 1964,
        "colors": ["red", "white", "blue"]
    }
    print(thisdict)
    print("--new-- print thisdict.items()")
    for x, y in thisdict.items():
        print(x, y)
    print("--new--mydict")
    mydict = thisdict.copy()
    print(mydict)
    print("--new--mydict2")
    mydict2 = dict(thisdict)
    print(f'mydict2=== {mydict2}')


    def my_function(input_1):
        return 5 * input_1


    print(my_function(3))
    print(my_function(5))
    print(my_function(9))


    def tri_recursion(k):
        if k > 0:
            result = k + tri_recursion(k - 1)
            print(f'Calculating the result ==> {result}')
        else:
            result = 0
        return result


    print("\n\nRecursion Example Results")
    print(f'final result is :{tri_recursion(3)}')

    print("--new--")


    def myfunc(n):
        return lambda a: a * n


    mydoubler = myfunc(2)
    mytripler = myfunc(3)
    print(mydoubler(11))
    print(mytripler(11))

    print("--new--")


    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return f"{self.name}({self.age})"
            print("Hello my name is " + self.name)


    p1 = Person("John", 36)
    print(p1)

    print("--new inheritance --")


    class Person:
        def __init__(self, fname, lname):
            self.firstname = fname
            self.lastname = lname

        def printname(self):
            print(self.firstname, self.lastname)


    class Student(Person):
        pass


    x = Student("Mike", "Olsen")
    x.printname()

    print("new")


    class Person:
        def __init__(self, fname, lname):
            self.firstname = fname
            self.lastname = lname

        def printname(self):
            print(self.firstname, self.lastname)


    class Student(Person):
        def __init__(self, fname, lname, year):
            super().__init__(fname, lname)
            self.graduationyear = year

        def welcome(self):
            print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


    x = Student("Mike", "Olsen", 2019)
    x.welcome()

    # import module file I created
    mymodule.greeting("Jonathan")

    # import date time module
    print("new-- printing noe time")
    x = datetime.datetime.now()
    print(x)
    x = datetime.datetime(1976, 5, 3)
    print(x)
    print(x.strftime("%c"))

    # sting prints
    age = 36
    name = "John"
    txt = "His name is {1}. {1} is {0} years old."
    print(txt.format(age, name))

    # file handling
    # f = open("demofile.txt", "r")
    # print(f.read(5))
    # print(f.readline())
    # print(f.read())
    # f.close()

    f = open("demofile2.txt", "w")
    f.write("Now the file has more content!")
    f.close()
    f = open("demofile2.txt", "r")
    print(f.read())

    f = open("demofile3.txt", "w")
    f.write("Now the file has more content!!!!!!!!")
    f.close()

    if os.path.exists("demofile.txt"):
        os.remove("demofile.txt")
    else:
        print("The file does not exist")

    # Finding LCM (Lowest Common Multiple)
    num1 = 4
    num2 = 6
    x2 = np.lcm(num1, num2)
    print(x2)

    # Finding GCD (Greatest Common Denominator),
    num1 = 6
    num2 = 9
    x2 = np.gcd(num1, num2)
    print(x2)

    arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
    x = np.unique(arr)
    print(x)

    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([3, 4, 5, 6])
    newarr = np.intersect1d(arr1, arr2, assume_unique=True)
    print(newarr)

    set1 = np.array([1, 2, 3, 4])
    set2 = np.array([3, 4, 5, 6])
    newarr = np.setxor1d(set1, set2, assume_unique=True)
    print(newarr)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
