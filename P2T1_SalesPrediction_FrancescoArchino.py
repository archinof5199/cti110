#this program estimates profit from total sales
#9/18/2017
#CTI-110 P2T1-sales prediction
#Francesco Archino
#

# Get the projected total sales.
total_sales =float(input("Enter the projected sales: "))

# Calculate the Profit as 23 percent of the total sales.
profit = total_sales * 0.23

#Display the Profit.
print("The Profit is $", format(profit, ",.2f"))
