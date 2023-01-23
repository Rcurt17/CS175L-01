SharesBoughtIni = 2000 # initially bought

PerShareIni = 40.00 # Cost initally

TotalIni = SharesBoughtIni * PerShareIni #total for paid shares

CommissionIni = 0.03 #percent for commission

StockbrokerCommissionIni = float(TotalIni * CommissionIni) #how much the commission was

print ("Amount paid for the stock is: $" ,format(TotalIni, ",.2f"))

print ("\n")

print ("Comission paid on the puchase is: $" ,format(StockbrokerCommissionIni, ",.2f"))

print ("\n")

# 2 weeks later

SharesSold = 2000

PerShare2WA = 42.75 #increase in price of the stock

Total2WA = SharesSold * PerShare2WA # how much after the increase in stock

Commission = 0.03 #same thing as CommissionIni

StockbrokerCommission = float(Total2WA * Commission) #how much stockbroker made

print("Amount the stock sold for: $",format(Total2WA, ",.2f"))

print ("\n")

print("Commission paid on the sale is: $" ,format(StockbrokerCommission, ",.2f"))

print ("\n")

profit = Total2WA - (TotalIni + StockbrokerCommissionIni + StockbrokerCommission)

print ("Profit (or loss if negative): $" ,format(profit, ",.2f"))
