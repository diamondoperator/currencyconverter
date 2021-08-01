#console program that converts USD to other top currencies

start_over = 1
while start_over < 2:
  print("Welcome to the currency converter")
  print("This console program will convert USD to Euros" +","+ "Yen"+","+ "British Pounds and Australian Dollars")
  print("------------------------------------------------------------------------------------------")
  print("Please enter the amount of United States Dollars you would like to convert: ")
  Usd = input()
  Euro  = round(float(Usd) * 0.85,2)
  Yen = round(float(Usd) * 110.08,2)
  Pounds = round(float(Usd) * 0.72,2)
  Australian_Dollar = round(float(Usd) * 1.36,2)
  print("\n")
  print("$"+ str(Usd) + " is equal to: ")
  print(str(Euro) + " Euros")
  print(str(Yen) + " Yen")
  print(str(Pounds) + " British Pounds")
  print(str(Australian_Dollar) + " Australian Dollars")
  print("------------------------------------------------------------------------------------------")


  question = input("Do you want to make another conversion? y/n: ")
  print("\n")

  if(question == "y"):
    start_over = 1

  else:
    start_over = 2
    print("Thanks for using this converter.")




