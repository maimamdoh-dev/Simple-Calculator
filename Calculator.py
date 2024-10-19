
number1 = int(input("Enter the First number :"))

number2 = int(input("Enter the Second number :"))

operator = input("Choose an operator (+ , - , * , /): ")

if operator == "+" :
    print("The Result is : " + str(number1 + number2))

elif operator == "-" :
    print("The Result is : " + str(number1 - number2))

elif operator == "*" :
    print("The Result is : " + str(number1 * number2))

elif operator == "/" :
    print("The Result is : " + str(number1 / number2))

else :
    print("Please , Choose from the operator options")

