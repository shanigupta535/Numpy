import numpy as np

a = np.array([10, 20, 30, 40])

print(a)
print(a * 2)
print(a.mean())

import numpy as np

gc_values = np.array([45.2, 51.8, 60.1, 48.5, 55.3])

print("Average GC Content:", np.mean(gc_values))
print("Highest GC Content:", np.max(gc_values))
print("Lowest GC Content:", np.min(gc_values))