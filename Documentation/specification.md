# Specification

### Author: Timothy S Falco
### Date  : 5/28/2026
#### Serial : CCFLLS-01-1.0
---
# Capacitive Coupling Field Liquid-Level Sensor iteration 1 version 1.0

## 1. Scope and Functional Requirement

This document defines the mechanical and electrical construction procedure for a chemically isolated capacitive liquid-level sensing system intended for continuous operation in biologically active aqueous environments. The system must maintain complete dielectric isolation between all conductive elements and the measured liquid while producing a stable analog signal proportional to fluid height.

---

## 2. System Architecture Overview

The sensor consists of two vertically aligned, electrically isolated capacitive probes arranged in parallel. One probe serves as the excitation electrode, while the second functions as the sensing electrode connected to an analog-to-digital measurement interface. The system operates using time-varying excitation at fixed frequency, producing a displacement-current-based response through a resistive measurement network.

---

## 3. Materials Specification

### 3.1 Structural Housing
- Potable-grade cross-linked polyethylene (PEX) tubing  
- Length: 3.8 inches per probe  
- Outer diameter: 0.6 inches  
- Inner diameter: 0.5 inches  

### 3.2 Internal Electrode
- Copper tubing core  
- Length: 3.8 inches (matched to PEX housing)  
- Outer diameter: approximately 0.5 inches  
- Inner diameter: approximately 0.45 inches  

### 3.3 Potting and Sealing Materials
- Aquarium-grade silicone elastomer (end sealing)  
- Fine silica sand (oven-dried, moisture-free filler)  
- Insulated hookup wire (low-leakage, high-flex preferred)  

---

## 4. Probe Fabrication Procedure

### 4.1 Copper Electrode Preparation
Each copper tube is mechanically abraded along its inner surface to improve electrical termination reliability. The prepared surface is then tinned using solder to create a stable internal electrical contact point for wiring attachment.

### 4.2 Electrical Termination
An insulated conductor is soldered to the prepared internal copper surface. The joint is mechanically stabilized and insulated such that no conductive material is exposed outside the probe body.

### 4.3 Mechanical Assembly
The copper tube is thermally press-fitted into the PEX housing. This creates a tight dielectric interface ensuring consistent capacitive coupling while maintaining full electrical isolation from the external environment.

---

## 5. Environmental Sealing Process

### 5.1 Internal Stabilization Fill
The internal void volume is filled with oven-dried fine silica sand prior to final sealing. This serves to:
- Reduce internal moisture condensation
- Increase mechanical damping
- Stabilize internal dielectric properties over time

### 5.2 End Sealing
Both ends of the PEX tube are sealed using aquarium-grade silicone elastomer. The seal must fully encapsulate wire exit points and prevent ingress of moisture or contaminants.

### 5.3 Curing
Sealed assemblies are allowed to fully cure under ambient conditions until elastomeric stability is achieved prior to deployment.

---

## 6. Probe Pair Configuration

Two identical probes are mounted in parallel vertical alignment with a fixed center-to-center spacing of approximately 0.1 inches. Mechanical mounting must ensure:
- No direct electrical coupling between probes
- Stable vertical orientation relative to liquid level
- No deformation of dielectric spacing under environmental load

---

## 7. Electrical Interface Specification

### 7.1 Excitation Stage
- Microcontroller: Raspberry Pi Pico or ESP32 family
- PWM excitation frequency: 50 kHz
- Duty configuration: 32768 (nominal mid-scale drive condition)
- Series excitation resistor: 47 kΩ

### 7.2 Sensing Stage
- Opposing probe connected to ADC input
- Pull-down resistor: 47 kΩ between ADC input and ground
- Measurement based on displacement current conversion through resistive load

---

## 8. Operating Principle Summary

The system operates through dielectric modulation of the electric field between probe electrodes. Effective capacitance increases with immersed probe length due to the permittivity contrast between air and water.

C(h) increases approximately linearly with submersion depth h.

The excitation waveform produces displacement current according to:

$$
I_C = C(dV/dt)
$$

which is converted into a measurable voltage across the resistive load network:

$$
V_ADC ≈ R · C(dV/dt)
$$

Resulting in an analog signal proportional to liquid level under fixed excitation conditions.

---

## 9. Final Assembly Requirements

- Ensure complete absence of exposed conductive material in contact with liquid  
- Maintain constant probe spacing during installation  
- Prevent mechanical stress on sealed end caps  
- Verify stable PWM excitation and ADC baseline prior to deployment  
- Confirm waterproof integrity before submersion testing  

---

## 10. Performance Constraint Summary

The sensor is designed for:
- Long-term submerged operation in conductive, contaminated, or biologically active water  
- Non-contact capacitive sensing only  
- Stable linear response over operational range  
- No electrolysis, galvanic reaction, or electrode degradation pathways