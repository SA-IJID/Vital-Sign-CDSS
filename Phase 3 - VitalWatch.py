
# VITAL SIGN 1: TEMPERATURE (CELCIUS)

print("Welcome To VitalWatch! ")

while True:  # open loop for repetitive code.

    # 1. creates the temp. float(input()) fxn (for both whole & decimals).
    temperature = float(input("Please Enter your temperature value: "))

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
    category = input("Enter Category (1/2/3): ")

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

    # EMERGENCY PATTERN: FINAL DIAGNOSIS BASED ON COMBINED VITALS

    bp_low = bp_status == "low"
    bp_high = bp_status in ["high", "elevated"]
    hr_low = hr_status == "low"
    hr_high = hr_status == "high"
    rr_high = rr_status == "high"
    rr_low = rr_status == "low"
    rr_irregular = rr_status != "normal"
    spo2_low = spo2_status in ["mild", "moderate", "low"]
    temp_low = temp_status == "low"
    temp_high = temp_status == "high"
    temp_normal = temp_status == "normal"

    if bp_low and hr_high and rr_high:  # emergency shock pattern.
        diagnosis = "Shock"
        likely_causes = ["Hypovolemic Shock",
                         "Septic Shock", "Cardiogenic Shock"]
        next_checks = [
            "Capillary refill, urine output (perfusion)",
            "Blood lactate (tissue hypoxia)",
            "Full blood count (Hb for bleeding, WBC for infection)",
            "Blood cultures (before antibiotics)",
            "Bedside ultrasound (FAST if trauma, cardiac function)",
            "ECG (rule out cardiac cause)"
        ]

    elif bp_high and hr_low and rr_irregular:  # Cushing's triad pattern.
        diagnosis = "Cushing’s Triad"
        likely_causes = ["Increased Intracranial Pressure"]
        next_checks = [
            "Glasgow Coma Scale (GCS)",
            "Pupillary size/reactivity",
            "Urgent CT scan (brain)",
            "Monitor oxygen saturation",
            "Check for head trauma history"
        ]

    elif rr_high and spo2_low:  # respiratory failure pattern.
        diagnosis = "Respiratory Failure"
        likely_causes = ["Pulmonary Embolism",
                         "Acute Respiratory Distress Syndrome"]
        next_checks = [
            "Arterial Blood Gas (ABG)",
            "Chest X-ray",
            "D-dimer (if PE suspected)",
            "CT pulmonary angiography (if stable)",
            "Lung auscultation"
        ]

    elif temp_high and hr_high and rr_high:  # systemic infection pattern.
        diagnosis = "Systemic Infection"
        likely_causes = ["Sepsis", "Malaria", "Pneumonia"]
        next_checks = [
            "Full blood count (WBC changes or severe sepsis) ",
            "Blood cultures",
            "Malaria test (RDT or smear)",
            "Chest X-ray",
            "CRP / Procalcitonin",
            "Serum lactate"
        ]

    elif temp_high and hr_low:  # relative bradycardia pattern.
        diagnosis = "Relative Bradycardia"
        likely_causes = ["Typhoid Fever", "Yellow Fever"]
        next_checks = [
            "Blood culture (typhoid confirmation)",
            "Widal test (supportive only)",
            "Liver function tests",
            "Travel/exposure history",
            "Viral PCR (if available)"
        ]

    elif bp_low and hr_high:  # early shock / volume loss.
        diagnosis = "Volume Loss / Early Shock"
        likely_causes = ["Dehydration", "Bleeding", "Early shock state"]
        next_checks = [
            "Packed Cell Volume (PCV) / Hemoglobin",
            "Urea & electrolytes (dehydration)",
            "Stool/urine check for blood loss",
            "IV fluid response monitoring"
        ]

    elif bp_low and hr_low:  # cardiac issue pattern.
        diagnosis = "Cardiac Issue"
        likely_causes = ["Heart Block", "Myocardial Infarction"]
        next_checks = [
            "ECG (critical)",
            "Cardiac enzymes (Troponin)",
            "Electrolytes (K⁺ abnormalities)",
            "Continuous cardiac monitoring"
        ]

    elif bp_high and hr_high:  # hyperdynamic state pattern.
        diagnosis = "Hyperdynamic State"
        likely_causes = ["Hyperthyroidism", "Pheochromocytoma"]
        next_checks = [
            "Thyroid function tests (TSH, T3, T4)",
            "Plasma metanephrines",
            "Blood glucose",
            "Drug/stimulant history"
        ]

    elif rr_high and temp_normal and not hr_high and not hr_low and not bp_low and not bp_high and spo2_status == "normal":
        diagnosis = "Early Warning Sign"
        likely_causes = ["Early respiratory distress",
                         "Compensated metabolic issue"]
        next_checks = [
            "ABG (look for metabolic acidosis)",
            "Blood glucose (DKA)",
            "Lactate",
            "Chest exam + X-ray"
        ]

    elif temp_normal and hr_high and not rr_high and not rr_low and bp_status == "normal" and spo2_status == "normal":
        diagnosis = "Panic vs Early Pathology"
        likely_causes = ["Anxiety", "Early organic cause"]
        next_checks = [
            "ECG",
            "Blood glucose",
            "Hemoglobin",
            "Then assess psychological cause"
        ]

    elif temp_low and hr_low and bp_low:  # hypothermia and low metabolism.
        diagnosis = "Severe Metabolic Suppression"
        likely_causes = ["Hypothermia"]
        next_checks = [
            "Core body temperature",
            "Blood glucose (hypoglycemia)",
            "Thyroid function (myxedema coma)",
            "Electrolytes",
            "Infection screen (late sepsis)"
        ]

    else:
        diagnosis = "No single emergency pattern detected"
        likely_causes = []
        next_checks = [
            "Continue monitoring and reassess if vital signs change."]

    print("\nFINAL DIAGNOSIS:")
    print(f"Diagnosis: {diagnosis}")

    if likely_causes:
        print("Possible Causes:")
        for cause in likely_causes:
            print(f"- {cause}")

    print("Next Checks:")
    for check in next_checks:
        print(f"- {check}")
    print()

    # 4. Closure of loop with condition with condition to continue.
    cc = input("Do you wish to continue? (yes/no): ")
    if cc.lower() == 'no':
        print("GoodBye! ")
        break  # 5. exit the entire code.
