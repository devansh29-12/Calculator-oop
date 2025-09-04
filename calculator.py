print("Welcome to the Calculator")

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    
    def sub(self):
        return self.num1 - self.num2
    
    def mul(self):
        return self.num1 * self.num2
    
    def div(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return "Error: Division by zero!"

def main():
    while True:
        print("\n--- Calculator Menu ---")
        print("Operations: +, -, *, /")
        print("Enter 'q' to quit")
        
        op = input("Enter operator: ")
        if op == "q":
            print("Exiting Calculator. Goodbye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number input. Try again.")
            continue

        calc = Calculator(num1, num2)

        if op == "+":
            print("Result:", calc.add())
        elif op == "-":
            print("Result:", calc.sub())
        elif op == "*":
            print("Result:", calc.mul())
        elif op == "/":
            print("Result:", calc.div())
        else:
            print("Invalid operator!")

if __name__ == "__main__":
    main()