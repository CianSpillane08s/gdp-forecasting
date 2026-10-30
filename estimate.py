# Forecasting
# Import WorldBank API
import wbgapi as wb # Don sonraí GDP

# Get the nation, change it into its code for example Germany -> DEU and find the amount of years in the future the user wants.
nation = input("what nation: ")
country_code = wb.economy.coder(nation)
years_in_future = int(input("How many years in the future? "))


# Get the GDP in 2025, the latest year
for row in wb.data.fetch('NY.GDP.MKTP.CD', country_code, "2025"):
    GDP_2025 = row['value']
   
   
# Faigh GDP an tír I 2024, an dara bliaian is deanaí
for row in wb.data.fetch('NY.GDP.MKTP.CD', country_code, "2024"):
    GDP_2024 = row['value']

#Find the rate of growth of GDP of that nation from 2024 to 2025
GDP_growth = ((GDP_2025 - GDP_2024) / GDP_2024) * 100
print(f"GDP growth equals {GDP_growth:.2f}%")


# Set GDP_INPUT to GDP_2025
GDP_INPUT = GDP_2025

# While "years_in_future" is greater then 1 the program keeps using the 24/25 growth rate to calculate the next year's GDP.
while years_in_future > 0:
    GDP_OUTPUT = GDP_INPUT * (1 + GDP_growth / 100)
    years_in_future -= 1
    GDP_INPUT = GDP_OUTPUT


# Output that nations estimated GDP in that year
print(f"The GDP of {nation} is: {round(GDP_OUTPUT, 2):,}$")


