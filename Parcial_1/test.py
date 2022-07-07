from email import header
import pandas as pd
from requests import head
# imporr scikit_learn as sk

# Not mutable variable
# Documentation: \assets\heart-disease.names
# DATA_PATH = 'Parcial_1\\assets\\diabetes.csv'
DATA_PATH = 'Parcial_1\\assets\\diabetes.csv'


# creating a dataframe
# the headers are in the first row
df = pd.read_csv(DATA_PATH, header=0)

# storing headers in a new panda series with the name of the column of df and store each unique value in it
headers = pd.Series(df.columns.values, name='headers')

# print(headers.head(10))
# creating a new dataframe with the headers and the unique values fo df

unique_values = []
for col in df:
    # print(df[col].unique())
    # store them in unique_values
    unique_values.append(df[col].unique().tolist())

# print(unique_values)    

# adding nan to unique_values in order to have the same size for each column
for i in range(len(unique_values)):
    if len(unique_values[i]) < len(unique_values[0]):
        unique_values[i].append(None)

# create a dictionary with the headers and the unique values
headers_dict = dict(zip(headers, unique_values))
# print(headers_dict)
# create a new dataframe with the headers and the unique values 
# unique_values_pd = pd.DataFrame(headers_dict)
# print(unique_values_pd)

# create unique_values_pd_prob with the same dimensions as unique_values_pd

# unique_values_pd_prob = pd.DataFrame(columns=unique_values_pd.columns)

print (df.head())
 # print the range of the values in each column

print ("----------------------------")
for col in df:
    print(col, df[col].min(), df[col].max())


