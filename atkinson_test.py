import concentration_library as cl
import pandas as pd

# Comparison with R version in IC2 package on hhbudget dataset
# Results
# Epsilon 0: 0
# Epsilon 1: 0.3245925
# Epsilon 2: 0.4951668
# Epsilon 3: 0.6053387
# Epsilon 4: 0.6856425

hhbudgets = pd.read_csv("hhbudgets.csv")
y = hhbudgets.as_matrix(columns=["ingreso"])
print(cl.atkinson(y, 0))
print(cl.atkinson(y, 1))
print(cl.atkinson(y, 2))
print(cl.atkinson(y, 3))
print(cl.atkinson(y, 4))
