# Capacitive Coupling Field Liquid-Level Sensor

A fully electrically isolated capacitive liquid-level sensing system designed for safe long-term submersion in livestock water or garden soil.

This repository contains the complete capacitive sensing system, including:

- Capacitive sensor probe specifications
- MicroPython software controller
- System integration documentation

These topics are introduced here only briefly. Detailed documentation for each component is provided in their respective directories and README files.

---

# Abstract

This project implements a non-contact capacitive liquid-level sensing system using sealed insulated probes and high-frequency capacitive coupling techniques.

The system is intended for environments where direct electrical contact with the measured liquid is undesirable or unacceptable, including conductive, contaminated, or biologically active water systems.

The design prioritizes:

- Complete electrical isolation from the liquid
- Long-term stability
- Potable-safe construction materials
- Low-cost manufacturability

---

# Sensor Probe System

The sensing assembly uses two parallel insulated probes constructed from sealed potable-safe PEX tubing with internal copper tube electrodes.

The probes operate through capacitive field coupling rather than direct conductive contact with the liquid.

Detailed probe dimensions, materials, construction procedures, and electrical characteristics are documented separately within the Documentation directory.

---

# Software Controller

The included MicroPython controller provides:

- PWM excitation signal generation
- ADC-based capacitive sensing
- Signal averaging and filtering
- Level normalization

Detailed API documentation and usage examples are provided in the controller-specific README.

---

# Repository Installation

## Clone Full Repository

```bash
git clone https://github.com/OCLAFLOPTSON/CCFLLS
```

---

## MicroPython Controller Only

```bash
git clone https://github.com/OCLAFLOPTSON/CCFLLS/Programming/CapacitiveSensor
```

Example Usage:

#### Working directory file structure:
    ├── CapacitiveSensor
    │   ├── __init__.py
    │   └──_cs.py
    ├── boot.py
    └── main.py

#### main.py:
```python
from time import sleep
from CapacitiveSensor import CapacitiveSensor

sensor = CapacitiveSensor(pwm=16, adc=26)

while True:
    print("\x1b[2J\x1b[H", end="")
    print(sensor.read())
    sleep(0.24)
```

---