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
# Create three objects of Item class
obj_1 = Item('Apple', 1.5, 10)
obj_2 = Item('Banana', 2, 2)
obj_3 = Item('Orange', 2.5, 1)

#‌ apply_discount method is called on obj_1
obj_1.apply_discount()
#‌ apply_discount method is called on obj_2
obj_2.apply_discount()
#‌ apply_discount method is called on obj_3
obj_3.apply_discount()

#‌ cualculate_total_price method is called on obj_1
print(obj_1.calculate_total_price())
#‌ cualculate_total_price method is called on obj_2
print(obj_2.calculate_total_price())
#‌ cualculate_total_price method is called on obj_3
print(obj_3.calculate_total_price())

# print the all list
print(Item.all)