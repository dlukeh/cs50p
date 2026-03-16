def main():
    # Prompt user for an arithmetic expression (e.g., "1 + 2")
    expression = input("Expression: ")

    # Split input into three parts: x (left operand), y (operator), z (right operand)
    x, y, z = expression.split()

    # Convert operands to floats
    x = float(x)
    z = float(z)

    # Perform the operation based on the operator
    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z

    # Print the result as a floating-point value with one decimal place
    print(f"{result:.1f}")


# Only run main() if this file is executed directly
if __name__ == "__main__":
    main()

