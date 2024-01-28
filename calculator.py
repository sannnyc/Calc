def addition(numb1,numb2):
    return numb1+numb2

def subtraction(numb1,numb2):
    return numb1-numb2

def multiplication(numb1,numb2):
    return numb1*numb2

def division(numb1,numb2):
    return numb1/numb2

while True:

    print("What would you like:")
    print("1.) Addition")
    print("2.) Subtraction")
    print("3.) Division")
    print("4.) Multiplication")
    print("5.) Press Q to Exit")

    choice = (input("\nWhat would you like to choose:"))

    if choice.lower() == "q":
        print("Goodbye")
        break

    try:
        choice = int(choice)

        numb1=float(input("Enter the first number:"))
        numb2=float(input("Enter the second number:"))

        result = None

        if choice == 1:
            result = addition(numb1,numb2)
        elif choice == 2:
            result = subtraction(numb1, numb2)
        elif choice == 3:
            result = division(numb1, numb2)
        elif choice == 4:
            result = multiplication(numb1, numb2)

        print ("your answer is", result)

    except ValueError:
        print("Something went wrong, please check the input")