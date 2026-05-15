# VitalSign-CDSS-Suite

A progressive Python-based **Clinical Decision Support System (CDSS)** designed to interpret patient vital signs and provide automated clinical alerts.

## Project Overview
This repository showcases the evolution of a medical tool designed to assist in the preliminary assessment of patient vitals. The project is divided into three distinct phases, demonstrating increasing complexity in logic and clinical parameters.

## Repository Structure

### 📂 Phase 1: ThermoPoint Core
The foundational script focused on **Body Temperature** interpretation.
* **Logic:** Categorizes inputs into Hypothermia, Normal, Low-Grade Fever, and High-Grade Fever.
* **Features:** Continuous input loop and immediate clinical advice based on temperature thresholds.

### 📂 Phase 2: VitalPoint
An expanded iteration adding **Pulse Rate (HR)** and **Oxygen Saturation (SpO2)**.
* **Logic:** Introduced age-stratified heart rate analysis (Neonatal vs. Adult).
* **Clinical Alerts:** Identifies Bradycardia and Tachycardia while providing specific action steps (e.g., assessing "The Big 3": Pain, Fever, or Dehydration).

### 📂 Phase 3: VitalWatch
The most advanced version, integrating **Respiration Rate (RR)** and refined oxygenation categories.
* **Sophistication:** Includes a demographic selection menu (Neonate, Maternal Adult, Non-maternal Adult) to ensure context-specific interpretation.
* **Safety:** Categorizes SpO2 levels from "Well-oxygenated" to "Medical Emergency!" with instructions for immediate clinical intervention.

## How to Run
1. Ensure you have **Python 3.x** installed.
2. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/VitalSign-CDSS-Suite.git](https://github.com/YOUR_USERNAME/VitalSign-CDSS-Suite.git)
   
   AUTHOR: Dr. Sajid. Medical Laboratory Scientist | Python Developer|Bioinformatics Enthusiast
