## dicts are grocery items, keys are name, cost, store, price, date of purchase, and date of final use(eaten/used for last time); still working on last one
from datetime import date, timedelta, datetime
#custom class
class Grocery():
	def __init__(self,buydate,name,price=0,usedate=None):
		self.buydate = buydate
		self.name = name
		self.price = price
		self.usedate = usedate
importList = []
#import from file as lists, to a list
with open('pantry.txt','r') as imp:
        for line in imp:
                importList.append(eval((line)))
pantryList = [Grocery(*x) for x in importList] #found this on stackexchange https://stackoverflow.com/questions/19307169/how-to-assign-a-class-object-to-a-item-in-a-list-python
#set alternate dates
month = '00'
day = '00'
year = '00'
def getmonth():
        global month
        month = str(input('Input month as mm\n'))
        if month.isdigit():
                if 0 < int(month) < 13:
                        if len(month) == 1:
                                month = '0'+month
                                print(month)
                        print('valid')
                else:
                        print('invalid input')
                        getmonth()
        else:
                print('invalid input')
                getmonth()
def getday():
        global day
        day = str(input('Input day as dd\n'))
        if day.isdigit():
                if month in ['01','03','05','07','08','10','12'] and 0 < int(day) < 32:
                        pass
                elif month in ['04','06','09','11'] and 0 < int(day) < 31:
                        pass
                elif month == '02' and 0 < int(day) < 29: #leap years, man
                        pass
                else:
                        print('invalid input')
                        getday()
                if len(day) == 1:
                        day = '0'+day
                        print(day)
                print('valid')
        else:
                print('invalid input')
                getday()
def getyear():
        global year
        year = str(input('Input year as yy\n'))
        if year.isdigit():
                if 0 <= int(year) < 100:
                        if len(year) == 1:
                                year = '0'+year
                                print(year)
                        print('valid')
                else:
                        print('invalid input')
                        getyear()                         
        else:
                print('invalid input')
                getyear()
#begin Item adding program        
def addItem():
        today = date.today().strftime('%m-%d-%y')
        print(today)
        toadd = str.lower(input('Add item from purchase? y/n \n'))
        newitem = []
        if toadd == 'y' or toadd == 'yes':
                dateask = str.lower(input('Item purchased today? y/n \n'))
                if dateask == 'y' or dateask == 'yes':
                        dateassign = today
                        newitem.append(dateassign)
                else:
                        def getdate():
                                getmonth()
                                getday()
                                getyear()
                                newdate = month +'-'+day+'-'+year
                                print(newdate)
                                newitem.append(newdate)
                                print(datetime.strptime(newdate,'%m-%d-%y')) #testing
                        getdate()
                        itemask = str.lower(input('Enter item name. \n'))
                        newitem.append(itemask)
                        try:
                                priceask = int(input('Enter item price. \n'))
                                newitem.append(priceask)
                        except:
                                print('Invalid price entered. \n')
        else:
                print('bye')

        print(newitem)
        importList.append(newitem)
        print(importList)
        print(pantryList)
        def updatelist():
                f = open('pantry.txt', 'w')
                for item in importList:
                        f.write(str(item)+'\n') #allows dictionaries to be written to file properly
                f.close()
        updatelist()
addItem()

#once items are added with datetimes, add functions for value
        # update class to have usedate attribute
        # find days between buydate and usedate
        # divide item price by days between purchase and final use to calculate value
        
#testing
today = date.today().strftime('%m-%d-%y')
todaycalc = datetime.strptime(today, '%m-%d-%y')
oneday = timedelta(days=1)

pantry0date = datetime.strptime(pantryList[0].buydate, '%m-%d-%y')
print(pantry0date)
print(pantry0date - oneday)

#print(pantryList[0].name,pantryList[0].buydate)
