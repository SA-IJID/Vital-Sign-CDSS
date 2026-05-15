# PHASE 2 - VitalPoint

print("WELCOME TO VITALPOINT! ")
while True:  # open loop for repetitive code.

    # VITAL SIGN 1: TEMPERATURE (CELCUIS)

    # 1. creates the temp. float(input()) fxn (for both whole & decimals).
    temperature = float(input("Enter your temperature value: "))

    if temperature < 35:  # first condition where temp. is below normal.
        temp_status = "low"
        print("Alert: Hypothermia")
        print("Action: Seek immediate warmth")

    # second condition where temp. is within normal ranges.
    elif 35 <= temperature <= 37.2:
        temp_status = "normal"
        print("Alert: Normal")
        print("Action: Stay Healthy!")

    # third condition where temp. is slightly abnormal.
    elif 37.3 <= temperature <= 38.4:
        temp_status = "high"
        print("Alert: Low-Grade Fever")
        print("Action: Rest and Get Hydrated.")

    else:  # fourth condition where temp. highly abnormal.
        temp_status = "high"
        print("Alert: High-Grade Fever")
        print("Action: Consult your Doctor")

    # VITAL SIGN 2: HEART RATE (PULSE)

    # 1. creates the age input function for categorization of pulse rate.
    age = input("Enter Client Age Group (1 for Neonate, 2 for Adult): ")

    # 2. creates the pulse input function for both whole numbers (integers) and categorization of pulse rate.
    pulse = int(input("Enter Pulse Rate (BPM): "))

    # first condition where client is a neonate (0-28 days) and pulse is below normal.
    if age == "1":
        if pulse < 100:
            hr_status = "low"
            print("Alert: NEONATAL BRADYCARDIA")
            print("Action: CHECK AIRWAY AND CONSIDER POSITIVE PRESSURE VENTILATION.")

        # second condition where client is a neonate (0-28 days) and pulse is within normal ranges.
        elif 100 <= pulse <= 160:
            hr_status = "normal"
            print("Alert: Normal Neonatal Pulse")
            print("Action: Routine Monitoring.")

        # third condition where client is a neonate (0-28 days) and pulse is above normal.
        else:
            hr_status = "high"
            print("Alert: NEONATAL TACHYCARDIA")
            print(
                "Action: CHECK TEMPERATURE, DEHYDRATION AND ASSESS IF INFANT DISTRESS/CRYING")

    elif age == "2":  # first condition where client is an adult and pulse is below normal.
        if pulse < 60:
            hr_status = "low"
            print("Alert: ADULT BRADYCARDIA")
            print("Action: ASSESS CLIENT IS DIZZY. CHECK FOR MEDICATIONS (BETA-BLOCKERS)")

        # second condition where client is an adult and pulse is within normal ranges.
        elif 60 <= pulse <= 100:
            hr_status = "normal"
            print("Alert: Normal Adult Pulse")
            print("Action: Routine Observation")

        else:  # third condition where client is an adult and pulse is above normal.
            hr_status = "high"
            print("Alert: ADULT TACHYCARDIA")
            print("Action: ASSESS 'THE BIG 3' PAIN, FEVER or DEHYDRATION")

    else:
        hr_status = "unknown"
        print("Alert: Unknown Age Group for Pulse Interpretation")
        print("Action: Use adult thresholds if appropriate.")

    # VITAL SIGN 3: OXYGEN SATURATION (SPO2)

    # 1. creates the spo2 input function for both whole numbers (integers) and categorization of spo2 levels.
    spo2 = int(input("Enter Client SPO2 %: "))

    if 95 <= spo2 <= 100:  # first condition where spo2 is within normal ranges.
        spo2_status = "normal"
        print("Alert: Normal")
        print("Action: Client is Well-oxygenated.")

    elif 91 <= spo2 <= 94:  # second condition where spo2 is slightly abnormal.
        spo2_status = "mild"
        print("Alert: Mild Hypoxia")
        print("Action: Monitor closely, client might need Supplementary Oxygen.")

    elif 86 <= spo2 <= 90:  # third condition where spo2 is moderately abnormal.
        spo2_status = "moderate"
        print("Alert: Moderate Hypoxia")
        print("Action: Immediate Clinical Assessment Required - Inform the Doctor with immediate effect")

    else:  # fourth condition where spo2 is severely abnormal.
        spo2_status = "low"
        print("Alert: SEVERE HYPOXIA")
        print("Action: MEDICAL EMERGENCY!")

    # VITAL SIGN 4: RESPIRATION RATE (BPM) -RR

    # 1. creates the category input function for categorization of respiration rate (RR) levels.
    print("Select Client Category: ")
    print("1. Neonate (0-28 Days) ")
    print("2. Maternal Adult")
    print("3. Non-maternal Adults")

    # 2. creates the category input function for categorization of respiration rate (RR) levels.
    category = input("Enter Category (1/ 2/ 3): ")

    # 3. creates the respiration rate input function for both whole numbers (integers) and categorization of respiration rate (RR) levels.
    rr = int(input("Enter Respiratory Rate (BPM): "))

    # first condition where client is a neonate (0-28 days) and respiration rate is above normal.
    if category == "1":
        if rr > 60:
            rr_status = "high"
            print("Alert: TACHYPNEA")
            print("Action: CHECK FOR NASAL FLARING AND ASSESS SPO2.")

        # second condition where client is a neonate (0-28 days) and respiration rate is within normal ranges.
        elif 40 <= rr <= 60:
            rr_status = "normal"
            print("Alert: Normal.")

        # third condition where client is a neonate (0-28 days) and respiration rate is below normal.
        else:
            rr_status = "low"
            print("Alert: BRADYPNEA")
            print("Action: CHECK AIRWAY.")

    # first condition where client is a maternal adult and respiration rate is above normal.
    elif category == "2":
        if rr > 24:
            rr_status = "high"
            print("Alert: TACHYPNEA")
            print("Action: CHECK FOR PAIN, ANXIETY AND SIGNS OF INFECTION.")

        # second condition where client is a maternal adult and respiration rate is within normal ranges.
        elif 16 <= rr <= 24:
            rr_status = "normal"
            print("Alert: Normal.")

        else:  # third condition where client is a maternal adult and respiration rate is below normal.
            rr_status = "low"
            print("Alert: BRADYPNEA")
            print("Action: EVALUATE SYSTEMIC STRESS OR FEVER.")

    # first condition where client is a non-maternal adult and respiration rate is above normal.
    elif category == "3":
        if rr > 20:
            rr_status = "high"
            print("Alert: TACHYPNEA")
            print("Action: CHECK FOR PAIN, ANXIETY AND SIGNS OF INFECTION.")

        # second condition where client is a non-maternal adult and respiration rate is within normal ranges.
        elif 12 <= rr <= 20:
            rr_status = "normal"
            print("Alert: Normal.")

        # third condition where client is a non-maternal adult and respiration rate is below normal.
        else:
            rr_status = "low"
            print("Alert: BRADYPNEA")
            print("Action: CHECK FOR MEDICATIONS EFFECT OR NEUROLOGICAL ISSUES.")

    else:
        rr_status = "unknown"
        print("Alert: Unknown category for respiratory rate interpretation")
        print("Action: Use adult thresholds if appropriate.")

    # VITAL SIGN 5: BLOOD PRESSURE (BP)

    # 1. creates the systolic blood pressure input function for both whole numbers (integers) and categorization of blood pressure levels.
    systolic = int(input("Enter Systolic BP (mmHg): "))

    # 2. creates the diastolic blood pressure input function for both whole numbers (integers) and categorization of blood pressure levels.
    diastolic = int(input("Enter Diastolic BP (mmHg): "))

    # first condition where blood pressure is below normal.
    if systolic < 90 or diastolic < 60:
        bp_status = "low"
        print("Alert: HYPOTENSION")
        print("Action: ASSESS FOR DIZZINESS, WEAKNESS AND CHECK FOR MEDICATIONS.")

    # 3. second condition where blood pressure is within normal ranges.
    elif 90 <= systolic <= 120 and 60 <= diastolic <= 80:
        bp_status = "normal"
        print("Alert: Normal")
        print("Action: Maintain Healthy Lifestyle.")

    # 4. third condition where blood pressure is slightly above normal.
    elif 120 < systolic <= 129 and diastolic < 80:
        bp_status = "elevated"
        print("Alert: ELEVATED BP")
        print("Action: Lifestyle Modifications Recommended.")

    # 5. fourth condition where blood pressure is moderately above normal.
    elif 130 <= systolic <= 139 or 80 <= diastolic <= 89:
        bp_status = "high"
        print("Alert: HYPERTENSION STAGE 1")
        print("Action: Monitor Regularly and Consider Lifestyle Changes.")

    # 6. fifth condition where blood pressure is significantly above normal.
    elif systolic >= 140 or diastolic >= 90:
        bp_status = "high"
        print("Alert: HYPERTENSION STAGE 2")
        print("Action: Consult Healthcare Provider for Management.")

    else:
        bp_status = "unknown"
        print("Alert: Unable to classify BP")
        print("Action: Double-check the BP readings.")

    # 3. Closure of loop with condition.
    choice = input("Do you wish to continue? (yes/no): ")
    if choice.lower() == 'no':
        print("GoodBye! ")
        break  # 4. exit the entire code
