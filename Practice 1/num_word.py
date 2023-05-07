# number = input("Enter a number: ")
# words = {'0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}

# for digit in number:
#     print(words[digit], end=' ')


number = input("Enter a number: ")

for digit in number:
    if digit == "0":
        print("Zero", end=" ")
    elif digit == "1":
        print("One", end=" ")
    elif digit == "2":
        print("Two", end=" ")
    elif digit == "3":
        print("Three", end=" ")
    elif digit == "4":
        print("Four", end=" ")
    elif digit == "5":
        print("Five", end=" ")
    elif digit == "6":
        print("Six", end=" ")
    elif digit == "7":
        print("Seven", end=" ")
    elif digit == "8":
        print("Eight", end=" ")
    elif digit == "9":
        print("Nine", end=" ")
