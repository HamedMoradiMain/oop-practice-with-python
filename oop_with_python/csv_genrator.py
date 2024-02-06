import random
import csv

fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Icedberry', 'Jackfruit']
prices = [round(random.uniform(1, 10), 2) for _ in range(10)]  # prices between 1 and 10
quantities = [random.randint(1, 100) for _ in range(10)]  # quantities between 1 and 100

with open('items.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'price', 'quantity'])
    for i in range(10):
        writer.writerow([fruits[i], prices[i], quantities[i]])