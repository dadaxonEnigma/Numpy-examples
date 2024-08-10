import numpy as np
## 1. Calculating Revenue
prices = np.array([19.99,29.99,14.99,9.99,24.99])
quantities = np.array([10,5,8,12,3])
revenue_per_product = prices * quantities
print(revenue_per_product)
total_revenue = np.sum(revenue_per_product)
print(total_revenue)