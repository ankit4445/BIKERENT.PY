class bikeshop:
    def __init__(self,stock):
        self.stock=stock

    def displayBike(self):
        print("Total Bikes",self.stock)

    def rentForBike(self,q):

        if q<=0:
            print("the quantity user can enter more than zero")
        elif q>self.stock:
            print("enter the value less than the stock")
        else:
            self.stock=self.stock-q
            print("Total prices",q*100)
            print("total bikes",self.stock)
while True:
    obj=bikeshop(120)
    uc=int(input('''
1. Display Stock
2. Rent a Bike
3. Exit    
    '''))
    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("enter the quantity..."))
        obj.rentForBike(n)
    else:
        break






