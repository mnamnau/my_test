# 2. Spočítejte, kolik procent z celkového rozpočtu je vyčerpáno 

import pandas as pd
import json

plan = pd.read_csv("1AHA810_plan.csv", sep = ";")
'''
data = plan.loc[:, 'Impressions_Client'] #do promenne data vypsat sloupec IC
print(data)
total_impressions_client = sum(data) #secteno IC
print(total_impressions_client)
'''
plan_result = {
    'total_impressions_client' : sum(plan.loc[:, 'Impressions_Client']),
    'total_clicks_client' : sum(plan.loc[:, 'Clicks_Client']),
    'total_views_client' : sum(plan.loc[:, 'Views_Client'])
}
'''
print(plan_result['total_impressions_client'])
#slovnik s klici
print(plan_result['total_impressions_client'])
print(plan_result['total_clicks_client'])
print(plan_result['total_views_client'])
'''
plan_result['total'] = plan_result['total_impressions_client'] + plan_result['total_clicks_client'] + plan_result['total_views_client']#nadefinovani dalsiho klice 'total'
#print(plan_result)
print("Total plan result is: " + str(round(plan_result['total'])))

postbuy = pd.read_csv("1AHA810_postbuy.csv", sep = ";")
postbuy_results = {
    'total_marketing_investment' : sum(postbuy.loc[:,'MarketingInvestment'])
}
#print(postbuy_results['total_marketing_investment']) 
#print(postbuy_results)
print("Total marketing investment is: " + str(round(postbuy_results['total_marketing_investment'])))

total = plan_result['total']
part_of_total = postbuy_results['total_marketing_investment']
total_percent = (part_of_total*100) / total
print("Vycerpano je " + str(round(total_percent)) + " % z celkoveho rozpoctu.")

'''
output = {
    "plan": plan_result,
    "postbuy": postbuy_results
}
with open("test.json", "w") as fp:
    json.dump(output, fp, indent = 2) 
'''