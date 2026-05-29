# CapacitiveSensor (CCFLLS Series Controller)

A MicroPython controller for capacitive coupling field liquid-level sensing systems.

It drives a PWM excitation signal and reads a corresponding ADC response to infer capacitive coupling changes in a probe system.

---

## License

MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Overview

This class implements:

- PWM excitation at fixed frequency (50 kHz)
- ADC sampling on a sensing electrode
- Averaged multi-sample readings
- Optional asynchronous continuous sampling loop using asyncio

The output value is a normalized averaged ADC reading representing relative signal strength on the sensing electrode.

---

## Hardware Model

This driver assumes:

- One GPIO pin outputs a PWM excitation signal
- One ADC-capable GPIO reads the sensing node
- The sensor is built to the CCFLLS-01-1.0 specification.

---

## Dependencies

MicroPython version 1.21+

---

## Class: CapacitiveSensor

### Constructor

CapacitiveSensor(pwm: int, adc: int)

Parameters:
- pwm: GPIO pin number used for PWM excitation
- adc: ADC pin number used for sensing input

Behavior:
- Initializes PWM at 50 kHz
- Sets 50% duty cycle (32768 / 65535)
- Initializes ADC input

---

## Methods

### _init_pwm()

Internal PWM configuration function.

- Frequency: 50,000 Hz
- Duty: 50%

Used automatically during initialization and reset.

---

### reset()

Forces the system into a known electrical state.

Steps:
- Sets PWM pin low
- Sets ADC pin low
- Waits 250 microseconds
- Reinitializes PWM
- Recreates ADC object

Purpose:
- Clears residual charge in the sensing system
- Stabilizes subsequent ADC readings

---

### read(samples=1000)

Blocking measurement function.

Parameters:
- samples: number of ADC samples to average

Returns:
- float: averaged and scaled ADC value (rounded to 2 decimal places)

Process:
- Calls reset()
- Reads ADC repeatedly
- Averages raw 16-bit readings
- Applies normalization

---

### Example Usage

``` python
from CapacitiveSensor import CapacitiveSensor

sensor = CapacitiveSensor(pwm=16, adc=26)

print(sensor.read())

# optionally use custom framerate
print(sensor.read(420))
```

#### Operate a relay

``` python
from CapacitiveSensor import CapacitiveSensor

sensor = CapacitiveSensor(pwm=16, adc=26)
relay = Pin(17, Pin.OUT)
THRESHOLD = 3.0

while True:
    # Relay HIGH until water level reaches THRESHOLD, then relay LOW
    # Example configuration: relay NC and COMMON on water pump positive(+)
    if sensor.read() < THRESHOLD:
        relay.value(1)
    else:
        relay.value(0)
```

---

## Notes

- Higher sample counts improve stability but increase latency
- Physical probe geometry dominates measurement behavior