#version 1 python virtual pet project
#melissaoneill
#24/04/

import time

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50

    def feed(self):
        self.hunger -= 10
        print(f"{self.name} has been fed.")

    def play(self):
        self.happiness += 10
        print(f"{self.name} is happy.")

    def status(self):
        print(f"{self.name}'s Hunger Level: {self.hunger}")
        print(f"{self.name}'s Happiness Level: {self.happiness}")

def main():
    pet_name = input("Enter your pet's name: ")
    pet = VirtualPet(pet_name)

    while True:
        print("\n1. Feed")
        print("2. Play")
        print("3. Check status")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.status()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

        # Simulate the passage of time
        time.sleep(1)

if __name__ == "__main__":
    main()

