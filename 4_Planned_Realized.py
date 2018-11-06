import matplotlib.pyplot as plt
import pandas as pd
import json
import csv

plan = pd.read_csv("1AHA810_plan.csv", sep = ";")
postbuy = pd.read_csv("1AHA810_postbuy.csv", sep = ";") 

# [
#  ["2/2/2018", 60000, 65000],
#  [date, plan_day_total, postbuy_day_total],
#  [x, y1, y2] 
# ] 
plot_data = [] 
for index, plan_row in plan.iterrows():
    plan_day_total = plan_row['Impressions_Client'] + plan_row['Clicks_Client'] + plan_row['Views_Client']
    
    postbuy_rows_in_day = postbuy.loc[postbuy['Date'] == plan_row['Date']]
    postbuy_day_total = sum(postbuy_rows_in_day.loc[:,'MarketingInvestment'])
    
    plot_data_row = [plan_row['Date'], plan_day_total, postbuy_day_total]
    plot_data.append(plot_data_row)

    
df_to_plot = pd.DataFrame(plot_data, columns=['Date','Plan','Investment'])
df_to_plot['Date'] = pd.to_datetime(df_to_plot['Date'], format="%d/%m/%Y")
df_to_plot_sorted = df_to_plot.sort_values(['Date'])

plot = df_to_plot_sorted.plot(use_index=False, x='Date', figsize=(20,10))
#plot.set_xticklabels(df_to_plot_sorted.Date)
plot.get_figure().savefig("plan_postbuy_days.png")