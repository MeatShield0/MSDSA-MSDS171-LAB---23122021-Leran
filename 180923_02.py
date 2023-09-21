# create a class restuarant that accepts iten name and quantity as input 
# inside your calss you are having the item and its price as a dictionary
# create a function calculate cost that prints the itemname, quantity and price

##Program
#creating a class
class restuarant:
    #initializing value of variables and creating a menu dictionary
    def __init__(self,item,qty):
        self.item = item
        self.qty = qty
        self.menu = {
            "rice":30,
            "Chicken":70
            }
    
    #logic part where we calculate qty * item
    def findCost(self):
        total=0
        total = self.qty * self.menu[self.item]
        print(self.item, self.qty, total)

order =  restuarant("rice",4)
order.findCost()
