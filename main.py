capacity=int(input("Enter the number of litres to fill the tank"))
dis =int(input("Enter the distance covered"))
if capacity>0 and dis>0:
    g = capacity * 0.2642
    m = 150 * 0.6214
    lk = (capacity / dis) * 100
    gm = (m / g)
    print("Litres/100KM {:.2f}".format(lk))
    print("Miles/gallons {:.2f}".format(gm))
else:
    print("Invalid input")
