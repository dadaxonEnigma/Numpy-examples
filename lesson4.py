## Categorizing product rating
import numpy as np
ratings = np.array([4.5,3.2,2.8,5.0,4.1,3.9,2.5,4.7])
positive_ratings = ratings[ratings >= 4.0]
print(positive_ratings)
negative_ratings = ratings[ratings < 4.0]
print(negative_ratings)