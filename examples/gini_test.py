import concentration_library as cl
import numpy as np

x = [541, 1463, 2445, 3438, 4437, 5401, 6392, 8304, 11904, 22261]


# Comparison with R version in ineq package
# Results
# Gini:             0.4620911
# Atkinson a=0.5:   0.1796591
# Atkinson a=1:     0.3518251

print(cl.gini(x))
print(cl.atkinson(x, 0.5))
print(cl.atkinson(x, 1.0))
