def camel_to_snake(camel_case):
    """
    Convert a camelCase string to snake_case.
    """
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case

camel = input("Enter the variable name in camel case: ")
print(camel_to_snake(camel))

