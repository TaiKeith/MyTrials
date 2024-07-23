from forex_python.converter import CurrencyRates

c = CurrencyRates()
amount = int(input("What is the amount to be converted?\n"))
from_currency = input("Which currency do you want to convert from: ").upper()
to_currency = input("Which currency do you want to convert to: ").upper()
converted_amount = c.convert(from_currency, to_currency, amount)
print(amount, from_currency, "=", converted_amount, to_currency)
