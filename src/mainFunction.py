def addition(number1, number2):
    return f"Addition of numbers is : {number1 + number2}"


def multiplication(number1, number2):
    return f"Multiplication of number : {number1 * number2}"


def findSubstring(masterString, subString):
    if masterString.__contains__(subString):
        print("substring found")
    else:
        print("substring not found")


if __name__ == '__main__':
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))
    add = addition(num1, num2)
    print(add)
    mul = multiplication(num1, num2)
    print(mul)
    findSubstring("python", "on")
