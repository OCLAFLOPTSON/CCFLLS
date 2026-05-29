# Abstract

### Author: Timothy S Falco
### Date  : 5/28/2026
#### Serial : CCFLLS-01-1.0
---
# Capacitive Coupling Field Liquid-Level Sensor iteration 1 version 1.0

A chemically isolated capacitive liquid-level sensor was developed for long-term operation in biologically active poultry pond environments where direct conductive contact between sensing electrodes and water is prohibited. The sensing assembly employs a dual-probe geometry consisting of two parallel insulated electrodes separated by approximately 0.1 in. Each probe is constructed from a 3.8 in length of potable-grade cross-linked polyethylene (PEX) tubing with nominal dimensions of 0.6 in outer diameter and 0.5 in inner diameter. A copper tube core of equal length and approximately 0.5 in outer diameter is thermally press-fitted within each PEX body to maximize dielectric coupling while maintaining complete electrical isolation from the external medium.

Electrical terminations are formed internally by soldering insulated conductors to abraded and tinned interior copper surfaces. The probes are environmentally sealed at both ends using aquarium-grade silicone elastomer. Residual internal void volume is filled with oven-dried fine silica sand prior to final sealing in order to reduce internal condensation, mechanical resonance, and dielectric instability. No conductive materials are exposed to the measured liquid at any point in the assembly.

Sensor operation is based upon field-coupled capacitance between the insulated probe pair. A pulse-width modulated excitation signal is applied to one probe while the opposing probe is connected to an analog measurement input through a resistive load network. Experimental operation was successfully demonstrated using a Raspberry Pi Pico microcontroller with a 50 kHz excitation frequency, a PWM duty value of 32768, a 47 kΩ series excitation resistor, and a 47 kΩ measurement pull-down resistor.

The sensing mechanism arises from the substantial difference in relative permittivity between air and water. The effective capacitance of the probe system varies approximately linearly with immersed probe length according to

$$
C(h)=C_{air}(L-h)+C_{water}h
$$

where $(L)$ represents total probe length, $(h)$ represents submerged length, and $(C_{air})$ and $(C_{water})$ represent distributed capacitance per unit length in air and water respectively. Because the dielectric constant of water greatly exceeds that of air, immersion produces a measurable increase in electric field coupling between probes.

The resulting displacement current is governed by

$$
I_C=C\frac{dV}{dt}
$$

where $(C)$ is the effective probe capacitance and $(\frac{dV}{dt})$ is the excitation edge rate produced by the PWM waveform. The measurement network converts this displacement current into a voltage response approximately described by

$$
V_{ADC}\approx RC\frac{dV}{dt}
$$

yielding an analog output that is approximately proportional to liquid level under fixed-frequency excitation conditions.

The sensor architecture demonstrates that stable liquid-level measurement may be achieved in conductive or contaminated aqueous environments without electrode exposure, electrolysis, galvanic contamination, or direct conductive sensing pathways. The use of inexpensive potable-safe materials combined with complete dielectric isolation provides a mechanically robust and chemically inert sensing platform suitable for long-duration agricultural and environmental monitoring applications.
