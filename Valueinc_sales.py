# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 09:29:10 2022

@author: linag
"""

import pandas as pd

#file_name = pd.read_csv("file.csv") Format of read.csv
data = pd.read_csv("transaction.csv")
data = pd.read_csv("transaction.csv",sep=";")
#summary of the data
data.info()

#working with calculations
#defining variables

CostPerItem = 11.73
SellingPricePerItem= 21.11
NumbersOfItemsPurchased = 6

#mathematical operations on tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = NumbersOfItemsPurchased * ProfitPerItem

CostPerTransaction = CostPerItem * NumbersOfItemsPurchased
SellingPricePerTransaction = SellingPricePerItem * NumbersOfItemsPurchased

# variable = dataframe["column_name"]

CostPerItem = data["CostPerItem"]
NumbersOfItemsPurchased = data["NumberOfItemsPurchased"]
CostPerTransaction = CostPerItem * NumbersOfItemsPurchased

#Adding new column to a dataframe

data["CostPerTransaction"] = CostPerTransaction
data["SalesPerTransaction"] = data["SellingPricePerItem"] * data["NumberOfItemsPurchased"]
 # Profit = sales - cost
 
data["ProfitPerTransaction"]= data["SalesPerTransaction"]-data["CostPerTransaction"]
data["MarkUpPerTransaction"]= data["ProfitPerTransaction"]/data["CostPerTransaction"]
 
RoundMarkup = round(data["MarkUpPerTransaction"],2)
data["MarkUpPerTransaction"]=round(data["MarkUpPerTransaction"],2)
 
 #concatenate data fields
 
day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)
date = day +"-" +data['Month'] + "-"+year
data['Date'] = date

#using iloc to view specific columns and rows
data.iloc[0]

data.iloc[-5:]#last five
data.head(5)#first five
data.iloc[:,2]#all rows specific column
data.iloc[4,2]#fourth row second column


#using split to split columns
#new_col = column.str.split('sep', expand = True)
split_col = data['ClientKeywords'].str.split(',', expand=True)


data.iloc[-1:]
#creating new columns for split_col
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#using the replace function
data['ClientAge'] = data['ClientAge'].str.replace("[","")
data['LengthOfContract'] = data['LengthOfContract'].str.replace("]","")


#changing letter case using lower function

data['ItemDesctiption']= data['ItemDescription'].str.lower()

seasons = pd.read_csv("value_inc_seasons.csv", sep=";")

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#drop columns df = df.drop ('columnname', axis = 1)

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Month', 'Year'], axis = 1)

#export into csv

data.to_csv('ValueInc_Cleaned.csv', index = False)


