#My first prototype in python #ThermoPoint Core - Phase 1

print("Welcome to ThermoPoint Core")

while True: #open loop for repetition...
    temperature = float(input("Please Enter your temperature value: "))  #1. creates the temp. float(input()) fxn (for both whole & decimals).
    
    if temperature < 35:  #first condition where temp. is below normal.
        print("Hypothermia")
        print("Seek immediate warmth")

    elif 35 <= temperature <= 37.2: #second condition where temp. is within normal ranges.
        print("Normal")
        print("Stay Healthy!")

#2. indentation of block code under loop from "if" to "else"

    elif 37.3 <= temperature <= 38.4:  #third condition where temp. is slightly abnormal.
        print("Low-Grade Fever")
        print("Rest and Get Hydrated.")

    else:  #fourth condition where temp. highly abnormal.
        print("High-Grade Fever")  
        print("Consult your Doctor")


    choice = input("Do you wish to continue? (yes/no): ")  #3. Closure of loop with condition.
    if choice.lower() == 'no' :
        print("GoodBye! ")
        break  #4. exit the entire code
    