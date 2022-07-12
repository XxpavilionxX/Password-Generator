import os.path
import random

# Randomize password with uppercase letters, lowercase letters, numbers, and special symbols
def password_randomizer():
    arr = []
    i, j, x, y = 0, 0, 0, 0
    numUpperCase, numLowerCase, numOfNumbers, numOfChars = 4, 3, 5, 2

    while i < numUpperCase:
        arr.append(chr(random.randint(65, 90)))
        i += 1

    while j < numLowerCase:
        arr.append(chr(random.randint(97, 122)))
        j += 1

    while x < numOfNumbers:
        arr.append(str(random.randint(0, 9)))
        x += 1

    while y < numOfChars:
        arr.append(chr(random.randint(33, 47)))
        y += 1

    random.shuffle(arr)
    password = "".join(arr)

    return password

# Write to passwords.txt file
def writeToFile(website):
    new_password = password_randomizer()
    with open(os.path.expanduser("~/Desktop/passwords.txt"), 'a') as file:
        file.write("{}: {}\n".format(website, new_password))


writeToFile("Youtube")