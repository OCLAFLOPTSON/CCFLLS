from machine import Pin, PWM, ADC
from asyncio import sleep
from time import sleep_us

class CapacitiveSensor:
    '''
    A controller for the CCFLLS series capacitive coupling field
    liquid-level sensors.
    
    #### alarm
        - if True, read() returns 0 if no water detected, 1 if water
        present anywhere on the sensor unit.
    
    #### read()
        - under normal operation returns float value corresponding to the
        voltage strength permittence of the sensor unit where 1.0 is open
        air and 3.3+ is fully submerged
    '''
    def __init__(self, pwm: int, adc: int, alarm: bool=False):
        self.alarm = alarm
        self._pwm_pin = pwm
        self._pwm = PWM(Pin(pwm))
        self._init_pwm()
        self._adc_pin = adc
        self._adc = ADC(Pin(adc))
    
    def _init_pwm(self):
        self._pwm.freq(50_000)
        self._pwm.duty_u16(32768)
    
    def reset(self):
        '''Pulls anode (PWM) and cathode (ADC) pins low and reinitializes
        respective objects'''
        Pin(self._pwm_pin, Pin.OUT).value(0)
        Pin(self._adc_pin, Pin.OUT).value(0)
        sleep_us(250)
        self._init_pwm()
        self._adc = ADC(Pin(self._adc_pin))
    
    def read(self, samples=1000):
        '''Return a float corresponding to the voltage strength on the
        cathode.'''
        total = 0
        if self.alarm:
            self.reset()
            for _ in range(samples):
                total += self._adc.read_u16()
            total = round(((total // samples) / samples), 2)
            return 0 if total >= 1.0 else 1
        for _ in range(samples):
            total += self._adc.read_u16()
        return round(((total // samples) / samples), 2)