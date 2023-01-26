#Raul Cortinas
#CS 175L
#1/26/2023
SharesBoughtIni = (float(input("Number of shares bought: "))) # initially bought

TotalMoneyforStock = (float(input("\nAmount per stock $: "))) #per share

CommissionIni = (float(input("\nCommission for the purchase %: "))) #commission

PaidIni = float(SharesBoughtIni * TotalMoneyforStock)

CommissionPaidIni = float(PaidIni * CommissionIni)

#2 weeks after

SharesSold = (float(input("\nNumber of shares sold after: "))) #Sold

StockPrice = (float(input("\nPrice of stock after: $")))

CommissionAfter = (float(input("\nComission for the sale %: ")))

PaidAfter = float(SharesSold*StockPrice)

CommissionPaidAfter = float(PaidAfter * CommissionAfter)

profit = PaidAfter - (PaidIni + CommissionPaidIni + CommissionPaidAfter)

print ("\nAmount paid for stock: $" , format(PaidIni, ",.2f"))

print ("\nCommission paid on the purchase: $", format(CommissionPaidIni, ",.2f"))

print("\nAmount the stock sold for: $", format(PaidAfter, ",.2f"))

print("\nCommission paid on the sale: $", format(CommissionPaidAfter, ",.2f"))

print("\nProfit (or loss if negative): $", format(profit, ",.2f"))

