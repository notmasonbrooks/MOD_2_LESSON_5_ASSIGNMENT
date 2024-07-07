
def calculator():

    while True:
        num_1 = int(input("Please enter a number: "))
        operation = input("Pick an operation: (+, -, *, /)")
        num_2 = int(input("Please enter another number: "))

        if operation == "+":
            total = (num_1 + num_2)
            print(f"{num_1} {operation} {num_2} = {total}")
        elif operation == "-":
            total = (num_1 - num_2)
            print(f"{num_1} {operation} {num_2} = {total}")
        elif operation == "*":
            total = (num_1 * num_2)
            print(f"{num_1} {operation} {num_2} = {total}")
        elif operation == "/":
            try:
                total = (num_1 / num_2)
            except ZeroDivisionError:
                total = None
            
            print(f"{num_1} {operation} {num_2} = {total}")
        break


        


calculator()        


