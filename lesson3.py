# Spliting Order into Batches
import numpy as np
order_ids = np.array([1001, 1002, 1003, 1004, 1005, 1006, 1007,1008])
print(order_ids)
batches = np.split(order_ids, 4)
print(batches)
for i, batch in enumerate(batches):
    print(f"Batch number {i}:")
    print("First element in the batch ", batch[0])
    print("Second element in the batch ", batch[1])
    print('')