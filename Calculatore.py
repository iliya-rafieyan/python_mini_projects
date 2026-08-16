# Calculatore

num1 = float(input('Enter firts number : '))
operator = input('select operators [+ - * / ** %]')
num2 = float(input('Enter second number'))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        pass
elif operator == "**":
    print(num1 ** num2)
elif operator == "%":
    print(num1 % num2)
