# -*- coding: utf-8 -*-
"""coffee bean sales analysis

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nnyK2stvdC3KqhDSTHPPx3t4xutihsk6
"""

#load_and_explorate

from google.colab import files
uploaded =files.upload()

import os
os.listdir()

import pandas as pd
df=pd.read_csv('DatasetForCoffeeSales2.csv')

df.head(20)

df.shape

df.info()

df.describe()

#clean_data

df["Date"]=pd.to_datetime(df["Date"])
print(df["Date"])

df.duplicated().sum()

df.isnull().sum()

df.isna()

#analysis_and_visualization

df_year =df.groupby(df["Date"].dt.to_period("Y"))["Final Sales"].sum()
df_year

df["monthly sales"]=df["Date"].dt.to_period("M").map(monthly_sales)
monthly_sales

df.head()

import matplotlib.pyplot as plt

monthly_sales=df.groupby(df["Date"].dt.to_period("M"))["Final Sales"].sum()
plt.figure(figsize=(10,4))
monthly_sales.plot(kind="line")
plt.title("monthly sales")
plt.show()

df.head()

plt.figure(figsize=(10,4))
df_year.plot(kind="bar")
plt.title("yearly sales")
plt.xlabel("year")
plt.ylabel("sales")
plt.show()

#Sales_by_product
Sales_by_product=df.groupby("Product")["Final Sales"].sum()


plt.figure(figsize=(10,4))
Sales_by_product.plot(kind="bar")
plt.title("sales by product")
plt.xlabel("product")
plt.ylabel("sales")
plt.show()

#QUANTITY_SOLD_BY_PRODUCT
QUANTITY_SOLD_BY_PRODUCT=df.groupby("Product")["Quantity"].sum()

plt.figure(figsize=(10,4))
QUANTITY_SOLD_BY_PRODUCT.plot(kind="bar")
plt.title("quantity sold by product")
plt.xlabel("peoduct")
plt.ylabel("quantity")
plt.show()

#top_customer_by_total_purshas
top_customer_by_total_purshas=df.groupby("Customer_ID")["Final Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(10,4))
top_customer_by_total_purshas.head(10).plot(kind="bar")
plt.title("top 10 customer by total purshas")
plt.xlabel("customer_id")
plt.ylabel("sales")
plt.show()

city_by_total_sold=df.groupby("City")["Sales Amount"].sum()

plt.figure(figsize=(10,4))
city_by_total_sold.plot(kind="bar")
plt.title("city by total sold")
plt.xlabel("city")
plt.ylabel("sales")
plt.show()

quantity_by_discount=df.groupby("Discount_Amount")["Quantity"].sum()

plt.figure(figsize=(10,4))
quantity_by_discount.plot(kind="line")
plt.title("quantity by discount")
plt.xlabel("discount")
plt.ylabel("quantity")
plt.xticks(rotation=90)
plt.show()

df.to_csv("cleaned_coffee_data.csv",index=False)

from google.colab import files
files.download("cleaned_coffee_data.csv")





