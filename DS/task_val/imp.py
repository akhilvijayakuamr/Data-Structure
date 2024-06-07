from Calcs.cal import *

while True:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    print("###################################")
    print("Select options : ")
    print("1 is Addition")
    print("2 is Substraction")
    print("3 is Multiplication")
    print("4 is Division")
    print("5 is stop the oprations")
    print("###################################")


    opr = int(input("Enter your choice: "))

    match opr:
        case 1:
            val=addition(num1, num2)
            print("The answer is ",val)

        case 2:
            val = substraction(num1, num2)
            print("The value is ", val)

        case 3:
            val = multiplication(num1, num2)
            print("The value is ", val)

        case 4:
            val = division(num1, num2)
            print("The value is ", val)
        case 5:
            break
        case _:
            print("Select proper choice !!!!!!!!!")
            