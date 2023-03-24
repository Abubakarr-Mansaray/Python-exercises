#!/bin/python3

# Ask user to input their weight on earth

earth_weight = float(input("Enter your weight on Earth (in kg): "))

# Define a dictionary with planet names as keys and their relative gravity as values

planet_gravity = {"Venus": 0.91, "Mars": 0.38, "Jupiter": 2.34, "Saturn": 1.06, "Uranus": 0.92, "Neptune": 1.19}

# Ask user to select a planet

print("Select a planet from the following list:")

for index, planet in enumerate(planet_gravity, start=1):

    print(f"{index}. {planet}")

planet_choice = int(input("Enter planet number: "))

# Calculate the weight of user on the selected planet

planet_name = list(planet_gravity.keys())[planet_choice - 1]

planet_weight = earth_weight * planet_gravity[planet_name]

# Print the weight of user on the selected planet

print(f"Your weight on {planet_name} is {planet_weight:.2f} kg.")


