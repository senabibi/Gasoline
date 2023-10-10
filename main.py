def find():
    gallon=float(input("Please enter the number of gallons of gasoline:"))
    print(f"Original number of gallons is:{gallon}")
    liter=gallon*3.7854
    print(f"{gallon} gallons is the equivalent of {liter} liters")
    barrel=42*gallon
    print(f"{gallon} gallons of gasoline requires {barrel} barrels of oil")
    gallon_of_gas=19.5*barrel
    print(f"{gallon} gallon of gasoline produces  {gallon_of_gas} pons of CO2")
    CO2=gallon_of_gas*20
    print(f"{gallon} gallon of gasoline produces {CO2} pounds of CO2")
    gallon_energy=gallon_of_gas*(115.000/75.700)
    print(f"{gallon} gallons of gasoline is energy equivalent to {gallon_energy} gallons of ethanol")
    cost=4*gallon
    print(f"{gallon} gallons of gasoline requires {cost} US dollars")
    print("Thanks for playing")
find()    