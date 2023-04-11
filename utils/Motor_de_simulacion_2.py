
import random

# Set up initial conditions
temperature = 20  # Celsius
precipitation = 5  # mm
sunlight = 8  # hours
growth_rate = 0  # cm/day
plant_height = 0  # cm
days = 30

# Simulate growth for each day
for day in range(1, days+1):
    # Randomly generate daily climate conditions
    temperature += random.uniform(-5, 5)
    precipitation += random.uniform(-2, 2)
    sunlight += random.uniform(-1, 1)
    
    # Calculate growth rate based on climate conditions
    if temperature > 20 and precipitation > 5 and sunlight > 6:
        growth_rate = random.uniform(0.1, 0.3)
    elif temperature > 18 and precipitation > 3 and sunlight > 4:
        growth_rate = random.uniform(0.05, 0.2)
    else:
        growth_rate = random.uniform(0, 0.05)
    
    # Calculate plant height based on growth rate
    plant_height += growth_rate
    
    # Print results for the day
    print(f"Day {day}: Temperature = {temperature:.2f}C, Precipitation = {precipitation:.2f}mm, Sunlight = {sunlight:.2f}h, Growth Rate = {growth_rate:.2f}cm/day, Plant Height = {plant_height:.2f}cm")
