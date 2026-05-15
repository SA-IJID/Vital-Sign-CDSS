# Convert if/elif statements to define a function for better modularity and readability.
def check_temperature(temp):
    if temp < 35:
        return "Hypothermia", "Seek immediate warmth"
    elif 35 <= temp <= 37.2:
        return "Normal", "Stay Healthy!"
    elif 37.3 <= temp <= 38.4:
        return "Low-Grade Fever", "Rest and Get Hydrated."
    elif 38.5 <= temp <= 40:
        return "High-Grade Fever", "Consult your Doctor"
    else:
        return "Invalid Temperature", "Please re-take the measurement."


print("Welcome to ThermoPoint 2.0")
user_temperature = float(input("\nPlease Enter your temperature value: "))
status, advice = check_temperature(user_temperature)
print(status)
print(advice)
while True:  # Open loop for repetition...
    choice = input("\nDo you wish to continue? (yes/no): ")
    if choice.lower() == 'no':
        print("Goodbye!")
        break  # Exit the entire code
    elif choice.lower() == 'yes':
        user_temperature = float(
            input("Please Enter your temperature value: "))
        status, advice = check_temperature(user_temperature)
        print(status)
        print(advice)
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
