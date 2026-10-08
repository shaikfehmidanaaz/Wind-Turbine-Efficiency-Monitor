class WindTurbineEfficiencyMonitor:

    def __init__(self, wind_speed, air_density, swept_area,
                 power_coefficient, generator_efficiency):
        self.wind_speed = wind_speed
        self.air_density = air_density
        self.swept_area = swept_area
        self.power_coefficient = power_coefficient
        self.generator_efficiency = generator_efficiency

    def calculate_wind_power(self):
        # Available power in the wind
        return 0.5 * self.air_density * self.swept_area * (self.wind_speed ** 3)

    def calculate_turbine_power(self):
        wind_power = self.calculate_wind_power()
        return wind_power * self.power_coefficient

    def calculate_electrical_power(self):
        turbine_power = self.calculate_turbine_power()
        return turbine_power * self.generator_efficiency

    def calculate_efficiency(self):
        wind_power = self.calculate_wind_power()
        electrical_power = self.calculate_electrical_power()

        if wind_power == 0:
            return 0

        return (electrical_power / wind_power) * 100

    def display_result(self):
        wind_power = self.calculate_wind_power()
        turbine_power = self.calculate_turbine_power()
        electrical_power = self.calculate_electrical_power()
        efficiency = self.calculate_efficiency()

        print("----- Wind Turbine Efficiency Monitor -----")
        print(f"Wind Speed              : {self.wind_speed:.2f} m/s")
        print(f"Air Density             : {self.air_density:.2f} kg/m³")
        print(f"Swept Area              : {self.swept_area:.2f} m²")
        print(f"Power Coefficient       : {self.power_coefficient:.2f}")
        print(f"Generator Efficiency   : {self.generator_efficiency * 100:.2f}%")

        print(f"\nAvailable Wind Power    : {wind_power:.2f} W")
        print(f"Turbine Mechanical Power: {turbine_power:.2f} W")
        print(f"Electrical Power        : {electrical_power:.2f} W")
        print(f"Overall Efficiency      : {efficiency:.2f}%")

        if efficiency >= 35:
            print("Status                  : HIGH EFFICIENCY")
        elif efficiency >= 25:
            print("Status                  : NORMAL EFFICIENCY")
        else:
            print("Status                  : LOW EFFICIENCY")


# Example values
wind_speed = 8                 # m/s
air_density = 1.225            # kg/m³
swept_area = 50                # m²
power_coefficient = 0.40       # Cp
generator_efficiency = 0.90    # 90%

monitor = WindTurbineEfficiencyMonitor(
    wind_speed,
    air_density,
    swept_area,
    power_coefficient,
    generator_efficiency
)

monitor.display_result()
