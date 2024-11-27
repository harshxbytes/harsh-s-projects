try:
    print("This is going to be a calculator app:-")
    numa = int(input("Enter the first number:-"))
    operend = input("Enter the openrand")
    numb = int(input("Enter the second number:-"))
    result = 0
    if operend == "+":
        result = numa + numb
    elif operend == "-":
        result = numa - numb
    elif operend == "*":
        result = numa * numb
    elif operend == "/":
        if numb == 0 or numa == 0:
            print("you cannot divide with zero(0)")
        
        result = numa / numb
    print(f"When {numa} will get {operend} by {numb} the answer is {result}")
    print("i am very happy as a programmer as someone is finding this shit useful")
except:
    print("you have entered the input in a wrong way")
    #this is my first project in python 