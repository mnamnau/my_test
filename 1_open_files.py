# 1. Načtěte data z plánu a postbuy 

import pandas as pd

plan = pd.read_csv("1AHA810_plan.csv", sep = ";")
print(plan.shape)
print(plan)

postbuy = pd.read_csv("1AHA810_postbuy.csv", sep = ";")
print(postbuy.shape)
print(postbuy)
