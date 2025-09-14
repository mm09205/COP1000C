kilowatt_hours = int(input("Enter kilowatt hours used: "))

if kilowatt_hours <= 1000:
    price_cents = kilowatt_hours * 7.633
    final_price = price_cents / 100 #convert to dollars
else:
    price_cents = 1000 * 7.633
    over_charge = (kilowatt_hours - 1000) * 9.259
    final_cents = price_cents + over_charge
    final_price = final_cents / 100 #convert to dollars

print(f"Amount owed is ${final_price:.2f}")


