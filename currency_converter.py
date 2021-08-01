#console program that converts USD to other top currencies

let Euro = Usd * 0.85
let Yen = Usd * 110.08
let Pounds = Usd * 0.72
let Australian Dollar = Usd * 1.36

let response = y
while response = y:
print("Welcome to the currency converter")
Print("This console program will convert USD to Euros, Yen, British Pounds and Australian Dollars"
)
print("------------------------------------------------------------------------------------------")
print("Please enter the amount of United States Dollars you would like to convert: ")
let Usd = input()
print("$"+ Usd + " is equal to: ")
print(Euro + "Euros")
print(Yen + "Yen")
print(Pounds + "British Pounds")
print(Australian Dollar + "Australian Dollars")
print("------------------------------------------------------------------------------------------")

print("/n")
print("Do you want to make another conversion? y/n ")
let response = input()

    if(response = "n")
    {
        print("Thanks for using this converter.")
    }