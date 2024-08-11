## Calculate Total and Avarage quantities sold
import numpy as np

#Each Column is specific product
#Each row is specific order
order_quantities = np.array([[5, 3, 2, 7],[10, 6, 3, 9]])
print(order_quantities)

#Quantities of the sales per product
total_quantities_sold = np.sum(order_quantities,axis=0)
print(total_quantities_sold)

#Quantities of the sales per order
total_products_per_order = np.sum(order_quantities,axis=1)
print(total_products_per_order)

#Average per product
average_quantities_sold = np.mean(order_quantities, axis=0)
print(average_quantities_sold)