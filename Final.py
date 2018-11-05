# 1. Načtěte data z plánu a postbuy #############################################

import pandas as pd
import statistics as stat
import json

#import plan
plan = pd.read_csv("1AHA810_plan.csv", sep = ";")
print(plan.shape)

#data = df.loc[:, 'Impressions_Client'] --->do promenne data vypsat sloupec IC
#total_impressions_client = sum(data) ---> secteno IC
#print(total_impressions_client)

plan_result = {
    'total_impressions_client' : sum(plan.loc[:, 'Impressions_Client']),
    'total_clicks_client' : sum(plan.loc[:, 'Clicks_Client']),
    'total_views_client' : sum(plan.loc[:, 'Views_Client'])
}
#print(plan_result['total_impressions_client'])

#slovnik s klici
#print(plan_result['total_impressions_client'])
#print(plan_result['total_clicks_client'])
#print(plan_result['total_views_client'])

plan_result['total'] = plan_result['total_impressions_client'] + plan_result['total_clicks_client'] + plan_result['total_views_client']#nadefinovani dalsiho klice 'total'
print(plan_result)

#import postbuy
postbuy = pd.read_csv("1AHA810_postbuy.csv", sep = ";")

print(postbuy.shape)

postbuy_results = {
    'total_marketing_investment' : sum(postbuy.loc[:,'MarketingInvestment'])
}
#print(postbuy_results['total_marketing_investment']) 
print(postbuy_results)

output = {
    "plan": plan_result,
    "postbuy": postbuy_results
}
with open("test.json", "w") as fp:
    json.dump(output, fp, indent = 2) 

# 2. Spočítejte, kolik procent z celkového rozpočtu je vyčerpáno #################

total = plan_result['total']
part_of_total = postbuy_results['total_marketing_investment']
total_percent = (part_of_total*100) / total
print(total_percent)

# 3. Spočítejte, kde jsme aktuálně časově v procentech, když počáteční datum (planu?) je 0% a koncové datum je 100%. 
import numpy as np
import pandas as pd
import csv
import json

plan = pd.read_csv("1AHA810_plan.csv", sep = ";")
print("plan shape")
print(plan.shape)

postbuy = pd.read_csv("1AHA810_postbuy.csv", sep = ";") 
#print(postbuy)
print("postbuy shape")
print(postbuy.shape)

plan_dates = plan['Date']#plan_dates = plan.select_column('Date')
#print(plan_dates)

not_broadcasted = []
broadcasted = []

for plan_date in plan_dates:
    #print("plan_date: " + plan_date)
    postbuy_row = postbuy.loc[postbuy['Date'] == plan_date]
    if(postbuy_row.empty is True) :
        not_broadcasted.append(plan_date)
        #not_broadcasted
        print("Not broadcasted : " + plan_date)
    else :
        broadcasted.append(plan_date)
        print("Broadcasted : " + plan_date)

print("Broadcasted total : " + str(len(not_broadcasted)))
print("Not broadcasted total : " + str(len(broadcasted)))
print(plan.shape[0])

output = {}
output['broadcasted'] = len(broadcasted)
output['not_broadcasted'] = len(not_broadcasted)
output['days_planned'] = int(plan.shape[0])

with open("broadcasted_not_broadcasted.json", "w") as fp:
    json.dump(output, fp, indent = 2) 


# Overeni, zda se kampan utraci spravne v case.
#"broadcasted": 302,
#"not_broadcasted": 62,
#"days_planned": 364

total = output['days_planned']
part_of_total_broadcasted = output['broadcasted']
total_percent_broadcasted = (part_of_total_broadcasted*100) / total
#print(total_percent_broadcasted)
print("Procentuelni podil odvysilanych kampani :" + str(round(total_percent_broadcasted)))

total = output['days_planned']
part_of_total_not_broadcasted = output['not_broadcasted']
total_percent_not_broadcasted = (part_of_total_not_broadcasted*100) / total
print("Procentuelni podil neodvysilanych kampani :" + str(round(total_percent_not_broadcasted)))





