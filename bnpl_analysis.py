import pandas as pd
import matplotlib.pyplot as plt

# Load data
sales_df = pd.read_csv('sales_data.csv')
survey_df = pd.read_csv('survey_data.csv')

# --- AOV Before and After BNPL ---
before_bnpl = sales_df[sales_df['BNPL_Used'] == 'No']['Order_Value'].mean()
after_bnpl = sales_df[sales_df['BNPL_Used'] == 'Yes']['Order_Value'].mean()

plt.figure(figsize=(6, 4))
plt.bar(['Before BNPL', 'After BNPL'], [before_bnpl, after_bnpl], color=['#8ecae6', '#219ebc'])
plt.title('Average Order Value Before and After BNPL Implementation')
plt.ylabel('AOV ($)')
plt.savefig('figures/Final_AOV_BNPL_Comparison.png')
plt.close()

# --- Monthly Orders Line Graph ---
monthly_orders = sales_df.groupby('Month')['Order_ID'].count()
plt.figure(figsize=(7, 4))
monthly_orders.plot(marker='o')
plt.title('Monthly Orders Before and After BNPL Implementation')
plt.xlabel('Month')
plt.ylabel('Number of Orders')
plt.grid(True)
plt.savefig('figures/Monthly_Orders_LineGraph.png')
plt.close()

# --- Customer Type Breakdown ---
bnpl_orders = sales_df[sales_df['BNPL_Used'] == 'Yes']
non_bnpl_orders = sales_df[sales_df['BNPL_Used'] == 'No']
first_time_bnpl = (bnpl_orders['Customer_Type'] == 'First-Time').mean() * 100
first_time_non_bnpl = (non_bnpl_orders['Customer_Type'] == 'First-Time').mean() * 100
repeat_bnpl = 100 - first_time_bnpl
repeat_non_bnpl = 100 - first_time_non_bnpl

import numpy as np
x = np.arange(2)
width = 0.35
plt.figure(figsize=(7, 4))
plt.bar(x, [first_time_bnpl, first_time_non_bnpl], width, label='First-Time Buyers')
plt.bar(x + width, [repeat_bnpl, repeat_non_bnpl], width, label='Repeat Buyers')
plt.xticks(x + width / 2, ['BNPL Orders', 'Non-BNPL Orders'])
plt.ylabel('Percentage of Orders')
plt.title('Customer Type by BNPL Usage')
plt.legend()
plt.savefig('figures/Final_BNPL_Customer_Breakdown.png')
plt.close()

# --- Survey: BNPL Purchase Decision Impact ---
impact_counts = survey_df['Would_Buy_Without_BNPL'].value_counts(normalize=True) * 100
plt.figure(figsize=(7, 4))
impact_counts.loc[['No', 'Yes']].reindex(['No', 'Yes']).plot(kind='bar', color=['#ffb703', '#219ebc'])
plt.title('Impact of BNPL on Purchase Decision')
plt.ylabel('Percentage of Respondents')
plt.xticks(ticks=[0,1], labels=['Would Not Purchase', 'Would Purchase Anyway'], rotation=0)
plt.savefig('figures/BNPL_Purchase_Impact_Graph_Fixed.png')
plt.close()
