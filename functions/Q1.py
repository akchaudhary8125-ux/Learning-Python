"""Write a function calculate() that:
Accepts two numbers and an operator (+, -, *, /)
Uses default parameter for operator as +
Returns the result
Handles division by zero gracefully"""


def calculate(n1, n2, op='+'):
    if (op == '+'):
        return n1 + n2
    elif (op == '-'):
        return n1 - n2
    elif (op == '*'):
        return n1 * n2
    elif (op == '/'):
        if (n2 == 0):
            return "Error"
        return n1/n2
    
    else:
        print("Invalid Operator")


print(calculate(5, 0, '/'))