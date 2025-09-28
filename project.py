from pyfiglet import Figlet
import random

figlet = Figlet()

class Animals:
    x = [
        "Cat", "Dog", "Pig", "Cow", "Horse", "Duck", "Sheep", "Goat",
        "Lion", "Tiger", "Bear", "Wolf", "Fox", "Rabbit", "Deer",
        "Monkey", "Elephant", "Giraffe", "Zebra", "Kangaroo", "Panda",
        "Otter", "Hedgehog", "Squirrel", "Chicken", "Turkey", "Donkey"
    ]
    
    @staticmethod
    def animal():
        print(random.choice(Animals.x), end="")
# Animals Class: Uses Method To Print Random Animal

class Locations:
    x = [
        "London", "Berlin", "Rome", "Cairo", "Vancouver", "Houston", "Belfast",
        "Paris", "Tokyo", "Sydney", "Barcelona", "Moscow", "Beijing", "Bangkok",
        "Amsterdam", "Lisbon", "Istanbul", "Seoul", "NewYork", "Chicago",
        "Mumbai", "Delhi", "CapeTown", "Rio", "Toronto", "Dubai", "Singapore"
    ]
    
    @staticmethod
    def location():
        print(random.choice(Locations.x), end="")
# Locations Class: Uses Method To Print Random Location

class Symbols:
    x = [
        "!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/",
        ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"
    ]
    
    @staticmethod
    def symbol():
        print(random.choice(Symbols.x), end="")
# Symbols Class: Uses Method To Print Random Symbol

class Numbers:
    @staticmethod
    def number():
        print(random.randint(0, 9), end="")
# Numbers Class: Uses Method To Print Random Number

def main():
    print(figlet.renderText("Memorable Password Generator")) # Prints Title Screen
    while True:
        input("Press Enter To Generate Password ") # Starts The Program
        Animals.animal() # Prints Random Animal
        Symbols.symbol() # Prints Random Symbol
        for _ in range(random.randint(1, 3)): 
            Numbers.number() # Prints A Random String Of Numbers 1-3 Digits Long
        Locations.location() # Prints Random Location
        Symbols.symbol() # Prints Random Symbol
        print("\n") # Moves Cursor Down
# Main Function: Carries Out The Process

if __name__ == "__main__":
    main() # Runs Main If The Correct File Is Open
