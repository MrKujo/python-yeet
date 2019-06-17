command = input("Add or subtract? ")

print("Let's " + command + " some numbers!")
yeet1 = input("Number 1: ")
yeet2 = input("Number 2: ")
numberyeet1 = int(yeet1)
numberyeet2 = int(yeet2)
if command == "add":
    result1 = numberyeet1 + numberyeet2
    output1 = str(result1)
elif command == "subtract":
    result2 = numberyeet1 - numberyeet2
    output2 = str(result2)
if command == "add":
    print(yeet1 + " + " + yeet2 + " = " + output1)
elif command == "subtract":
    print(yeet1 + " - " + yeet2 + " = " + output2)
