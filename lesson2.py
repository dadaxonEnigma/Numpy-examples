## Analyzing Blog Post Stats
import numpy as np
views = np.array([1000,500,1000,4444,2222,600])
max_views = np.max(views)
print(max_views)
min_views = np.min(views)
print(min_views)
avarage_views = np.round(np.mean(views),2)
print(avarage_views)
