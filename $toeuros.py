"""""
this program takes the dollar amount entered by the user and converts it to euros
made by acadia babcook
"""
Dollar = 0
Euros = 0
def Converter():
    Dollar= float(input("Enter dollar amount to be converted: "))
    Euros = Dollar* .94540
    print("$" + str(Dollar)+" Dollars" + " is equivelant to:  %s"%(u"\N{euro sign}") + str(Euros) + " Euros")
# title
print ("Dollar to Euro money converter")
while True:
    userinput = input("Would you like to convert dollars to euros? Yes or No ")
    if userinput == "yes":
        Converter()
    else:
        break