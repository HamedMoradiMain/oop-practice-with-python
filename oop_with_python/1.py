import csv 
class Item:
    pay_rate = 0.8 #‌ pay_rate is a class attribute
    all = [] # all is a class attribute
    def __init__(self,name:str,price:float,quantity:int=0):
        #‌ Run validation for received data
        assert price >= 0, f'Price must be greater or equal to 0, but got {price}'
        assert quantity >= 0, f'Quantity must be greater or equal to 0, but got {quantity}'
        #‌ Assign received data to object's attributes
        self.name = name
        self.price = price
        self.quantity = quantity
        # Append the created object to the all list
        Item.all.append(self)
    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    # the __repr__ method is called when the object is printed
    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv",'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)
            for item in items:
                item = Item(item['name'],float(item['price']),int(item['quantity']))
    # static methods
    @staticmethod 
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


item = Item.instantiate_from_csv()
print(Item.all)