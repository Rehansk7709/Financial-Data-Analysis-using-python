#capstone project of financial data using python
# we will   loadinng->,  cleaning-> transformation ->  and  we will do aggregation-> visualization
########################################## IMOPRTING LIBRARIES ########################################################################################################
import pandas as pd 
import numpy as np
import  matplotlib.pyplot as plt
import seaborn as  sns 
############################################# DATA EXPLORATION  (LOADING DATA) #######################################################################################################
# this step is for loading the data from the csv file into a pandas DataFrame. 
df = pd.read_csv('C:\\Users\\REHAN RIYAZ SHEIKH\\Downloads\\Synthetic_Financial_datasets_log.csv.zip')

#############################################   DATA CLEANING ########################################################################################

#df.head() is used to display the first 5 rows of the DataFrame. It is useful for quickly inspecting the data and understanding its structure.
#df.info() is used to display a concise summary of the DataFrame, including the number of non-null entries, data types of each column, and memory usage. It helps in understanding the overall structure and characteristics of the dataset.
print(df.head())
print(df.info())

# df.isnull().sum() is used to check for missing values in the dataset. It will return a Series with the count of missing values for each column in the DataFrame.
print(df.isnull().sum())

# df.drop_duplicates(inplace=True) is used to remove duplicate rows from the DataFrame. The inplace=True parameter ensures that the changes are made directly to the original DataFrame without creating a new one.
df.drop_duplicates(inplace=True)
print(df.info())

######################################################### DATA TRANSFORMATION  ##########################################################################################
# feature engineering - new column addion
# categorization - group of numeric data for better analysis.
df['NEW_COLUMN_Amount_Category'] = pd.cut(df['amount'], bins=[0, 5000, 10000, 20000], labels=['Low', 'Medium', 'High'])
print(df.head())




######################################################### DATA AGGREGATION  ####################################################################
transcation_summary = df.groupby("type").agg(
    total_amount=("amount","sum"),
    avg_amount=("amount","mean"),
    count_trans=("amount","count")
).reset_index()# RESET INDEX IF FOR BETTER VISUALIZATION  pc will give us result on their index so we done  reset_index() to reset the index of the aggregated DataFrame.  

print(transcation_summary)

######################################################## step6 visuzliation - bar plot , histogram, scatter plot ##############################################

plt.figure(figsize=(10,6))
sns.barplot(x="type",y="total_amount",data=transcation_summary)
plt.title("banks data for amount groups")
plt.show()
