
num1 = float(input("Enter the 1st number: "))
operator = input("Enter an operator (+ - * /): ")
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not valid operator")





score = float(input("Enter the student's score (0-100): "))

if 90 <= score <= 100:
    print("Grade A")
elif 80 <= score < 90:
    print("Grade B")
elif 70 <= score < 80:
    print("Grade C")
elif 60 <= score < 70:
    print("Grade D")
elif 0 <= score < 60:
    print("Grade F")
else:
    print("Invalid score! Please enter a value between 0 and 100.")