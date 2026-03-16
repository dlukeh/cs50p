def convert():
    userInput=input("Enter some text: ")
    userInput=userInput.replace(":)", "🙂")
    userInput=userInput.replace(":(", "🙁")
    print(userInput)

convert()

