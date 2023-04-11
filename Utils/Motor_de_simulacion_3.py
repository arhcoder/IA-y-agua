# Define function to calculate growth rate based on climate conditions
def calculate_growth_rate(temperature, precipitation, sunlight):
    if temperature > 20 and precipitation > 5 and sunlight > 6:
        return 0.3
    elif temperature > 18 and precipitation > 3 and sunlight > 4:
        return 0.15
    else:
        return 0.05

# Set up initial conditions
plant_height = 0  # cm

# Simulate growth for each day
while True:
    # Get climate data for the day
    temperature = float(input("Enter temperature (Celsius): "))
    precipitation = float(input("Enter precipitation (mm): "))
    sunlight = float(input("Enter sunlight (hours): "))
    
    # Calculate growth rate based on climate conditions
    growth_rate = calculate_growth_rate(temperature, precipitation, sunlight)
    
    # Calculate plant height based on growth rate
    plant_height += growth_rate
    
    # Print results for the day
    print(f"Growth Rate = {growth_rate:.2f}cm/day, Plant Height = {plant_height:.2f}cm")
    
    # Ask if user wants to continue or end simulation
    answer = input("Continue (Y/N)? ")
    if answer.lower() == "n":
        break