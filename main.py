#defining pet class 
#has stats for hunger, energy and happiness
import time
import random

class Pet: 
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50

    def feed(self):
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} feels full now!")

    def play(self):
        self.energy -= 10
        self.happiness += 10
        if self.energy < 0:
            self.energy = 0
        print(f"{self.name} had a great time playing!")

    def sleep(self):
        self.energy += 10
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} feels well rested after sleeping")

    def check_status(self):
        print(f"{self.name}'s status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")

def main():
    pet_name = input("Enter your pet's name: ")
    pet = Pet(pet_name)
    print(f"Welcome, {pet.name}!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Sleep")
        print("4. Check status")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.sleep()
        elif choice == '4':
            pet.check_status()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        # Simulating time
        time.sleep(1)
        pet.hunger += random.randint(0, 5)
        pet.energy -= random.randint(0, 5)
        pet.happiness -= random.randint(0, 5)

        if pet.hunger > 100:
            pet.hunger = 100
        if pet.energy < 0:
            pet.energy = 0
        if pet.happiness < 0:
            pet.happiness = 0

if __name__ == "__main__":
    main()
