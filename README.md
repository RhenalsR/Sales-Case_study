# Sales-Case_study

In this Case Study a Sales Dataset was used to respond to some business questions and analyse trends using Python and Tableu.

### Questions for the Analysis
- What is the general sales trend?
- What are the top 10 products by sales?
- Which are the most selling products?
- Which are the most profitable categories and sub-categories?

## Data Preparation

In this opportunity, I'm using a Retail Datased of a global superstore (not specified) for a 4-year period, between 2011-01-01 and 2014-12-31.
This dataset contains 51289 rows and 21 columns. And it's available on [Kaggle](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting).

This time I used Python to analyse the data, so I started importing Libraries and the Dataset

```
# Data manipulation
import pandas as pd

# Data visualization
import matplotlib.pyplot as plt

import seaborn as sns
```
 
```
# Importing Dataset
df = pd.read_excel('superstore_sales.xlsx')
```

## Processing

Let's take a first sight of the data

```
# checking first 5 rows of the Dataset
df.head(5)
```
![Preview of head limited to 5 rows](/head_table.png)
```
# checking last 5 rows of the Dataset
df.tail(5)
```
![Preview of tail limited to 5 rows](/tail_table.png)
```
# summary of the dataset
df.info()
```
![Preview of table description](/data_info.png)

With this summary, I encountered this dataset is pretty clean, there are no Null values and the data types are correct. However, I'd rather to check duplicates before going further

```
# looking for duplicates
duplicate = df[df.duplicated()]
 
print("Duplicate Rows :")
duplicate
```
No duplicate values were encountered. Lastly, let's check the descriptive statistics of the data.

```
# Getting a descriptive statistic summary
df.describe()
```
![Preview of table statistic summary description](/stat_summ.png)
## Analysis

- What is the general sales trend?

First I'm checking some information to better understand the timeframe (context), minimums, and maximums.
```
df['order_date'].max()
```
```
df['order_date'].min()
```
Now, the date formatting is YYYY-MM-DD hh:mm:ss, as I'm going to analyze just year and month it's better to change the format to YYYY-MM
```
# getting only month and year
df['month_year'] = df['order_date'].apply(lambda x: x.strftime('%Y-%m'))
```
then grouping data
```
# Grouping by Month-Year
df_trend = df.groupby('month_year').sum()['sales'].reset_index()
```
Visualizing:

```
plt.figure(figsize=(15, 6))
plt.plot(df_trend['month_year'], df_trend['sales'])
plt.xticks(rotation=45, size=8)    
plt.show
```
![Preview of sales trend viz](/py_viz.png)
Answering the question:
It's visible how sales trend is growing, sales are rising. We can also notice that sales get higher at the end of the year.

- What are the top 10 products by sales
Organizing
```
# Grouping product name
prod_sales =  pd.DataFrame(df.groupby('product_name').sum()['sales'])
```
```
# Sorting descending
prod_sales = prod_sales.sort_values('sales', ascending=False)
```
Checking the table, and here's the top 10:
```
prod_sales[:10]
```
![Preview of the top 10 products table](/top_10_table.png)
- Which are the most selling products?
```
# Grouping
most_sell_prod = pd.DataFrame(df.groupby('product_name').sum()['quantity'])
```
```
# Sorting descending
most_sell_prod = most_sell_prod.sort_values('quantity', ascending=False)
```
Let's take the top 15 this time
```
most_sell_prod[:15]
```
![Preview of the 15 best sellers](/best_sell_table.png)

- Which are the most profitable categories and sub-categories?
```
cat_profit = pd.DataFrame(df.groupby(['category', 'sub_category']).sum()['profit'])
```
Result:
```
cat_profit.sort_values(['category', 'profit'], ascending=False)
```
![Preview of the most profitable categories and sub-categories](/cat_profit_table.png)

Check out the Jupyter Notebook to further check the dataset, tables and outputs.

## Visualizing

Additionally, I'm creating some visualizations and a Dashboard with some filters using Tableau.

Previously we've seen the overall sales trend, now I wanted to re-visualize within quarters instead of months and add the profit values to the viz.

 ![Preview of the Tableau viz](/Viz_1.png)

Here we can also see the higher sales trend in the last quarter of each year.
Now, I created a Dashboard to check specific values as the Stakeholders would like to see:

![Preview of the Tableau Dashboard](/Dashboard.png)

Let's now take a look at the trend of Phones sold in the US.

![Preview of the Tableau Dashboard](/Dashboard_filt.png)

Feel free to take a look at the [Tableau Dashboard](https://public.tableau.com/app/profile/ramses.rhenals/viz/Superstoresales_16929203324650/Dashboard1) and try some filters yourself, like the Art Sales in France.

## _Thanks for reading!_
