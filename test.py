# Testing
import wbgapi as wb # Don sonraí GDP


nation = input("Cén tír: ")
country_code = wb.economy.coder(nation)
years_in_future = int(input("Cé mhead bliain sa todhcaí 1-3? "))


for row in wb.data.fetch('NY.GDP.MKTP.CD', country_code, "2025"):
    GDP_2025 = row['value']
   

for row in wb.data.fetch('NY.GDP.MKTP.CD', country_code, "2024"):
    GDP_2024 = row['value']


for row in wb.data.fetch('NY.GDP.MKTP.CD', country_code, "2023"):
    GDP_2023 = row['value']


for row in wb.data.fetch('NY.GDP.MKTP.CD', country_code, "2022"):
    GDP_2022 = row['value']
   

for row in wb.data.fetch('NY.GDP.MKTP.CD', country_code, "2021"):
    GDP_2021 = row['value']


E_GDP_growth = ((GDP_2022 - GDP_2021) / GDP_2021) * 100
print(f"GDP growth equals {E_GDP_growth:.2f}%")



if years_in_future == 1:
    REAL_GDP = GDP_2023
elif years_in_future == 2:
    REAL_GDP = GDP_2024
elif years_in_future == 3:
    REAL_GDP = GDP_2025
else:
    print("earraid san ionchuir")

GDP_INPUT = GDP_2022

while years_in_future > 0:
    GDP_OUTPUT = GDP_INPUT * (1 + E_GDP_growth / 100)
    years_in_future -= 1
    GDP_INPUT = GDP_OUTPUT

error = abs(GDP_OUTPUT - REAL_GDP) / REAL_GDP * 100
accuracy = 100 - error

print(f"An cruinneas ná {round(accuracy, 3)}")
