#This program calculates meal+tip+tax for total cost
#9 september 2019
#CTI-120 P2HW1 - meal tip tax calculator
#Francesco Vincent Archino
#

meal = float ( input ("please enter meal cost without tax or tip:"))

tip = float ( input ("please enter tip in decimal format:"))

tax = float ( input ("please enter tax in decimal format:"))

tip_tax_total = (tip + tax)

print("tip and tax total is" , tip_tax_total)

print("total meal with tip and tax is")

totalmealcost = (tip + tax + meal)

print("total meal cost is" , totalmealcost)

input()


