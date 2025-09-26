print("Enter your first number: ")
num1 = float(input())
print("Enter your second number: ")
num2 = float(input())
print("Enter an operator (+, -, *, /): ")
operator = input()

if operator == '+':
	result = num1 + num2
elif operator == '-':
	result = num1 - num2
elif operator == '*':
	result = num1 * num2
elif operator == '/':
	if num2 != 0:
		result = num1 / num2
	else:
		result = "Error: Division by zero"
else:
	result = "Invalid operator"

print("Result:", result)
