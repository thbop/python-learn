
def execute_operation(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    
    elif operation == "-":
        return num1 - num2
    
    elif operation == "*":
        return num1 * num2
    
    elif operation == "/":
        return num1 / num2

def square_root(x):
    x_i0 = x
    while True:
        x_i1 = x_i0 - ( x_i0*x_i0 - x ) / ( 2*x_i0 )
        if (abs(x_i0 - x_i1) < 1.0e-12):
            return x_i1
        x_i0 = x_i1

def nth_root(x, n):
    x_i0 = x
    while True:
        x_i1 = x_i0 - ( x_i0**n - x ) / ( n*x_i0**(n-1) )
        if (abs(x_i0 - x_i1) < 1.0e-12):
            return x_i1
        x_i0 = x_i1


def calc():
    num1 = float(input("Enter a number: "))


    while True:
        operation = input("Enter a operation: ")
        if operation == '=':
            break
        num2 = float(input("Enter a number: "))
        num1 = execute_operation(num1, num2, operation)
        print("num1", num1)
    
    print(num1)

    
if __name__ == "__main__":
    calc()
    # print(f((6.625 + 6.75) / 2))