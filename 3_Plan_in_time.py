# 3. Spočítejte, kde jsme aktuálně časově v procentech, když počáteční datum (planu?) je 0% a koncové datum je 100%. 
import numpy as np
import pandas as pd
import csv
import json

plan = pd.read_csv("1AHA810_plan.csv", sep = ";")
postbuy = pd.read_csv("1AHA810_postbuy.csv", sep = ";") 

plan_dates = plan['Date']

not_broadcasted = []
broadcasted = []

for plan_date in plan_dates:
    ##print("Plan date: " + plan_date)
    postbuy_row = postbuy.loc[postbuy['Date'] == plan_date]
    if(postbuy_row.empty is True) :
        not_broadcasted.append(plan_date)
        #print("Not broadcasted : " + plan_date)
    else :
        broadcasted.append(plan_date)
        #print("Broadcasted : " + plan_date)

print("Broadcasted total : " + str(len(not_broadcasted)))
print("Not broadcasted total : " + str(len(broadcasted)))

output = {}
output['broadcasted'] = len(broadcasted)
output['not_broadcasted'] = len(not_broadcasted)
output['days_planned'] = int(plan.shape[0])

with open("broadcasted_not_broadcasted.json", "w") as fp:
    json.dump(output, fp, indent = 2) 

total = output['days_planned']
part_of_total_broadcasted = output['broadcasted']
total_percent_broadcasted = (part_of_total_broadcasted*100) / total

print("Podil odvysilanych kampani je " + str(round(total_percent_broadcasted)) + " % z celkoveho rozpoctu.")

