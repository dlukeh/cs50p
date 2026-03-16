word = input("Input: ")

result = ""

for char in word:
    if char.lower() not in "aeiou":
        result += char

print(result)

