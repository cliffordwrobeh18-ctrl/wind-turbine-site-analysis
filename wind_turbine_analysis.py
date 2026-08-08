"""Core wind-turbine calculations from an ENGR 1102 project."""
import numpy as np

CP = 0.53
RADIUS = 75.0
R = 287
H1 = 10.0
H2 = 100.0
Z0 = 1.6
CUT_IN = 3.5
CUT_OUT = 20.0

def air_density(temp_c, pressure_mbar):
    temp_k = temp_c + 273.15
    pressure_pa = pressure_mbar * 100
    return pressure_pa / (R * temp_k)

def adjust_wind_speed(wind_speed):
    return wind_speed * (np.log(H2 / Z0) / np.log(H1 / Z0))

def turbine_power_kw(temp_c, pressure_mbar, wind_speed):
    rho = air_density(temp_c, pressure_mbar)
    v2 = adjust_wind_speed(wind_speed)
    if v2 < CUT_IN or v2 > CUT_OUT:
        return 0.0
    area = np.pi * RADIUS**2
    power_watts = 0.5 * CP * rho * area * v2**3
    return power_watts / 1000

if __name__ == "__main__":
    temperature = 0.2
    pressure = 1016
    measured_wind_speed = 0.3
    print(f"Adjusted wind speed: {adjust_wind_speed(measured_wind_speed):.3f} m/s")
    print(f"Estimated turbine power: {turbine_power_kw(temperature, pressure, measured_wind_speed):.2f} kW")
