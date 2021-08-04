"""Restaurant rating lister."""


# put your code here
import random
import os

pathing = './ratings/'
folder = os.listdir(pathing)
files = []

currentFile = 0

restaurantRating = {}
sortedRestaurantRating = {}

def init():
    global folder
    print("Please select one of the following numbers:\n")
    for i in range(len(folder)):
        files.append(pathing + folder[i])
    toDict(files[currentFile])
    sortAlphabetRatings(restaurantRating)


def alterFiles():
    global currentFile
    global folder
    print("Please select one of the following numbers:\n")
    for i in range(len(folder)):
        print(str(i + 1) + ".", folder[i])
        if pathing + folder[i] not in files:
            files.append(pathing + folder[i])
    option = int(input("Option: "))
    currentFile = option - 1
    toDict(pathing + folder[option - 1])
    sortedRestaurantRating.clear()
    sortAlphabetRatings(restaurantRating)


# print(lines)
def toDict(file):
    text = open(file)
    restaurantRating.clear()
    lines = text.read().split('\n')
    for line in lines:
        line = line.split(':')
        # print(line)
        if line[0] != '':
            restaurantRating[line[0]] = line[1]

# print(restaurantRating)


def sortAlphabetRatings(rating):
    for key in sorted(rating):
        sortedRestaurantRating[key] = rating[key]


def printDict(dict):
    for key in dict:
        print(key, ':', dict[key])


def addRating():
    key = input("Please input the restraurant name: ")
    value = int(input("Please input the restraurant score between the values of 1 and 5: "))
    while value > 5 or value < 1:
        print("Sorry, that value is not between 1 and 5.")
        value = int(input("Please input the restraurant score between the values of 1 and 5: "))
    name = key.split(" ")
    key = ""
    for word in name:
        key = key + word.capitalize()
        if word != name[-1]:
            key = key + " "
    restaurantRating[key] = value
    sortedRestaurantRating.clear()
    sortAlphabetRatings(restaurantRating)


def chooseRestaurantScore():
    keys = list(sortedRestaurantRating)
    print("Please select one of the following numbers:\n")
    for i in range(len(keys)):
        print(str(i + 1) + ".", keys[i] + ":", sortedRestaurantRating[keys[i]])
    option = int(input("Option: "))
    newScore(keys[option - 1])


def randomRestaurantScore():
    keys = list(sortedRestaurantRating)
    option = random.randint(0, len(keys))
    newScore(keys[option])


def newScore(key):
    restaurantRating[key] = input(f"Please input a new score for {key}: ")
    sortAlphabetRatings(restaurantRating)


def main():
    init()

    while True:
        print(f"The current file is {os.path.basename(files[currentFile])}: ")
        option = int(input("""Please select one of the following numbers: 
        1: Alter files.
        2: Show the restaurants and their ratings.
        3: Add a new restaurant and its rating.
        4: Update a random restaurant.
        5: Update a restaurant.
        6: Quit this program.
        Option: """))
        if option == 1:
            alterFiles()
        elif option == 2:
            printDict(sortedRestaurantRating)
        elif option == 3:
            addRating()
        elif option == 4:
            randomRestaurantScore()
        elif option == 5:
            chooseRestaurantScore()
        elif option == 6:
            exit()

main()