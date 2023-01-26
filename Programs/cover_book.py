#FRB December 7, 2022
#ThinkPython2e 2.10 Exercise
#Create a function that adds the total wholesale cost and shipping price of a book

#These are global variables that will appear in the function
coverPrice = 24.95
totalCopies = 60
addl_copies = 59
discount = .40
shipping = 3
addl_shipping = 0.75

#The function is defined and is empty since there is nothing inside the wholesalePrice()
def wholesalePrice():
                
                wholeSale = coverPrice * discount
                shipping_costs = wholeSale + shipping
                addl_shippingCost = addl_shipping * addl_copies
                ShippingTotal = shipping + addl_shippingCost
                TotalWholeSale = ((addl_copies * wholeSale) + wholeSale)
                print("You ordered", totalCopies, "copies of the book.")
                print("The wholesale cost is $", wholeSale)
                print("The additional copies cost $", addl_copies * wholeSale)
                print("The total wholesale cost of the books without shipping is ${:.2f}" .format(TotalWholeSale))
                print("Shipping for the first copy cost $", shipping)
                print("The additional shipping cost $", addl_shippingCost)
                print("The shipping total is ${:.2f}".format(ShippingTotal))
                print("The total wholesale cost with total shipping is ${:.2f}".format(TotalWholeSale + ShippingTotal))
                
                
                
                
                
#Call the wholesalePrice() function                
wholesalePrice()

#Print statements that require the user's input.  The program will pause after each input statement until the user responds.
print()
print("That is your complete invoice.")
print()
print()
pause = input("Press Any key to continue")
print()
orderCheck = input("Is your order correct? : ")
print()
feedback = input("Does this complete your order: " )
