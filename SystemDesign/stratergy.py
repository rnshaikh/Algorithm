"""

The strategy method is Behavioral Design pattern that allows you to define the complete family of algorithms, 
It enables selecting the algorithm at run-time. This method is also called as Policy Method.

"""



from abc import ABC, abstractmethod


class Stratergy(ABC):
    
    @abstractmethod
    def pay(self):
        pass
    

class CreditCardPay(Stratergy):
    
    def pay(self, amount):
        print("pay by credit card", amount)
        

class PaypalPay(Stratergy):
    
    def pay(self, amount):
        print("pay by paypal", amount)
        
        
class Item:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
        
        
class Cart:
    
    def __init__(self):
        self.items = []
        
    def add_items(self, item):
        self.items.append(item)
        
    
    def calculate_total(self):
        total = 0
        for obj in self.items:
            total += obj.price
            
        return total
    
    def pay(self, PayStratergy):
        
        total = self.calculate_total()
        PayStratergy.pay(total)
        
        
        
cart = Cart()
item1 = Item("tshirt", 100)
item2 = Item("pant",1000)

cart.add_items(item1)
cart.add_items(item2)

paypal = PaypalPay()
credit = CreditCardPay()

cart.pay(paypal)
cart.pay(credit)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        




