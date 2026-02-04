import re

HISTORY_FILE = "history.txt"

def show_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            lines = file.readlines()
            if not lines:
                print("No history found!")
            else:
                for line in reversed(lines):
                    print(line.strip())
    except FileNotFoundError:
        print("No history found!")

def clear_history():
    with open(HISTORY_FILE, 'w'):
        pass
    print("History cleared.")

def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(f"{equation} = {result}\n")

def calculate(user_input):
    parts = [p.strip() for p in re.split(r'(\+|\-|\*|/)', user_input)]

    if len(parts) != 3:
        print("Invalid input. Use format: number operator number (e.g. 8+8 or 8 + 8)")
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Please enter valid numbers.")
        return

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Use only +, -, *, /")
        return

    if result.is_integer():
        result = int(result)

    print("Result:", result)
    save_to_history(user_input, result)

def main():
    print("-- SIMPLE CALCULATOR (type history, clear or exit) --")
    while True:
        user_input = input(
            "Enter calculation (+ - * /) or command (history, clear, exit): "
        )

        if user_input == "exit":
            print("Goodbye!")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)

main()
