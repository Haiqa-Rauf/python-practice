# Problem 1:Temperature Converter & Logic
#(Write a script temperature.py that converts temperatures between Celsius and Fahrenheit.)
# 1. Define a function convert_temperature(temp, unit):
#   ~  If unit is "C", convert temp to Fahrenheit ($F = C \times \frac{9}{5} + 32$).
#   ~  If unit is "F", convert temp to Celsius ($C = (F - 32) \times \frac{5}{9}$).
# 2. Add input validation using raise ValueError if an invalid unit (anything other than "C" or "F") is passed.
# 3. Wrap your code execution in a try...except block to catch and handle any ValueError gracefully.
def convert_temperature(temp, unit):
    if unit == "C":
        return temp * 9/ 5 + 32
    elif unit == "F":
        return (temp - 32) * 5 / 9
    else:
        raise ValueError("Invalid unit. Use 'C' or 'F'.")

try:
    temp = float(input("Enter temperature: "))
    unit = input("Enter unit (C/F): ").upper()
    result = convert_temperature(temp, unit)
    print(f"Converted temperature: {result}")
except ValueError as e:
    print(f"Error: {e}")
