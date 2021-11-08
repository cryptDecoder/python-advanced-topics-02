import datetime
import time
from src.importFunction import callFunction

callFunction()


def variableTypeIdentifier():
    name = "jake"
    age = 45
    salary = 345655.90
    married = True
    print(f"Type of name : {type(name)}")
    print(f"Type of age : {type(age)}")
    print(f"Type of salary : {type(salary)}")
    print(f"Type of married : {type(married)}")


def fullName(f_name, l_name):
    print(f"Full name : {f_name} {l_name}")
    pass


def returnValue(number):
    return number * 2


def currentDatetime():
    print(f"Current datetime : {datetime.datetime.now()}")


fullName("jake", "Jordan")
variableTypeIdentifier()
number = int(input("Enter your number : "))
result = returnValue(number)
result = result + 10
print(f"Multiplication : {result}")
time.sleep(10)
currentDatetime()
