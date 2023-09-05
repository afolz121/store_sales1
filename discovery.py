#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

# %%

train = pd.read_csv('train.csv')
oil = pd.read_csv('oil.csv')
test = pd.read_csv('test.csv')
holidays = pd.read_csv('holidays_events.csv')
stores = pd.read_csv('stores.csv')
transactions = pd.read_csv('transactions.csv')
samp_sub = pd.read_csv('sample_submission.csv')

# %%

train['date'] = pd.to_datetime(train['date'])

#how many sotres and famlies

print(train['store_nbr'].nunique(), train['family'].nunique())
# 
# %%

train_store_sales = pd.DataFrame(train.groupby(['store_nbr','date'])['sales'].sum()).reset_index()
# %%

sns.lineplot(data = train_store_sales, x = 'date',\
             y = 'sales', \
                hue = 'store_nbr')
# %%
plt.figure(figsize = (12,8))
sns.barplot(data = train_store_sales, x = 'date', y = 'sales')
# %%
plt.figure(figsize = (12,8))
sns.lineplot(data= train_store_sales, x = 'date', y = 'sales')
# %%

def get_month_year(data) :
    output = []
    for row in data :
        output.append(str(row.year) + '-' + str(row.month))
    return output

# %%

train_store_sales['year_month'] = get_month_year(train_store_sales['date'])
# %%

sales_by_month = pd.DataFrame(train_store_sales.groupby('year_month')['sales'].sum()).reset_index()

sales_by_month['year_month'] = pd.to_datetime(sales_by_month['year_month'])
sales_by_month.head()

sales_by_month = sales_by_month.sort_values('year_month')
# %%
plt.figure(figsize = (12,8))
sns.lineplot(data = sales_by_month, x = 'year_month', y = 'sales')
# %%

