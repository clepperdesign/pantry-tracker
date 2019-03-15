## dicts are grocery items, keys are name, cost, store, price, date of purchase, and date of final use(eaten/used for last time); still working on last one
from datetime import date
from datetime import timedelta
#custom class
class Grocery():
	def __init__(self,name,store,price=0,buydate= date.today()):
		self.name = name
		self.store = store
		self.price = price
		self.buydate = buydate

importList = []
#import from file as lists, to a list
with open('pantry.txt','r') as imp:
        for line in imp:
                importList.append(eval((line),{"__builtins__":None},{})) #making sure eval can't be abused

pantryList = [Grocery(*x) for x in importList] #found this on stackexchange https://stackoverflow.com/questions/19307169/how-to-assign-a-class-object-to-a-item-in-a-list-python

#testing
print(importList)
print(pantryList)
print(pantryList[0].name,pantryList[0].buydate)
