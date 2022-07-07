from email import header
import pandas as pd
from requests import head
import numpy as np
# Not mutable variable
# Documentation: \assets\heart-disease.names
# DATA_PATH = 'Parcial_1\\assets\\diabetes.csv'
DATA_PATH = 'Parcial_1\\assets\\diabetesTest.csv'


df = pd.read_csv(DATA_PATH, header=0)
headers = pd.Series(df.columns.values, name='headers')


unique_values = []
for col in df:
    unique_values.append(df[col].unique().tolist())

for i in range(len(unique_values)-1):
    if len(unique_values[i]) < len(unique_values[0]):
        unique_values[i].append(None)
headers_dict = dict(zip(headers, unique_values))

print (df.head())
 # print the range of the values in each column except the last column

print ("----------------------------")
for col in df:
    if col == 'class':
        break
    print(col, df[col].min(), df[col].max())
    # print(np.linspace(df[col].min(),df[col].max(),4))

# values to discretize the data

# preg 0 17
# [ 0.          5.66666667 11.33333333 17.        ]
# plas 0 199
# [  0.          66.33333333 132.66666667 199.        ]
# pres 0 122
# [  0.          40.66666667  81.33333333 122.        ]
# skin 0 99
# [ 0. 33. 66. 99.]
# insu 0 846
# [  0. 282. 564. 846.]
# mass 0.0 67.1
# [ 0.         22.36666667 44.73333333 67.1       ]
# pedi 0.078 2.42
# [0.078      0.85866667 1.63933333 2.42      ]
# age 21 81
# [21. 41. 61. 81.]

# discretizing the data



df_discretized = df.copy()

# if preg column is not null, discretize it
# if preg>=0 and preg<5.66666667,               preg=1
# if preg>=5.66666667 and preg<11.33333333,     preg=2
# if preg>=11.33333333 and preg<17.0,           preg=3
# if preg>=17.0,                                preg=4

# if plas column is not null, discretize it
# if plas>=0 and plas<66.33333333,              plas=1
# if plas>=66.33333333 and plas<132.66666667,   plas=2
# if plas>=132.66666667 and plas<199.0,         plas=3
# if plas>=199.0,                               plas=4

# if pres column is not null, discretize it
# if pres>=0 and pres<40.66666667,              pres=1
# if pres>=40.66666667 and pres<81.33333333,    pres=2
# if pres>=81.33333333 and pres<122.0,          pres=3
# if pres>=122.0,                               pres=4

# if skin column is not null, discretize it
# if skin>=0 and skin<33.0,                      skin=1
# if skin>=33.0 and skin<66.0,                   skin=2
# if skin>=66.0 and skin<99.0,                   skin=3
# if skin>=99.0,                                 skin=4

# if insu column is not null, discretize it
# if insu>=0 and insu<282.0,                     insu=1
# if insu>=282.0 and insu<564.0,                 insu=2
# if insu>=564.0 and insu<846.0,                 insu=3
# if insu>=846.0,                                insu=4

# if mass column is not null, discretize it
# if mass>=0 and mass<22.36666667,               mass=1
# if mass>=22.36666667 and mass<44.73333333,     mass=2
# if mass>=44.73333333 and mass<67.1,            mass=3
# if mass>=67.1,                                 mass=4

# if pedi column is not null, discretize it
# if pedi>=0.078 and pedi<0.85866667,             pedi=1
# if pedi>=0.85866667 and pedi<1.63933333,        pedi=2
# if pedi>=1.63933333 and pedi<2.42,              pedi=3
# if pedi>=2.42,                                  pedi=4

# if age column is not null, discretize it
# if age>=21 and age<41,                          age=1
# if age>=41 and age<61,                          age=2
# if age>=61 and age<81,                          age=3
# if age>=81,                                     age=4

# iterating the rows of df in order to discretize the data

for index, row in df.iterrows():
    for col in df:
        if col == 'class':
            continue
        if row[col] is not None:
            if col == 'preg':
                if row[col] >= 0 and row[col] < 5.66666667:
                    df_discretized.at[index, col] = 1
                elif row[col] >= 5.66666667 and row[col] < 11.33333333:
                    df_discretized.at[index, col] = 2
                elif row[col] >= 11.33333333 and row[col] < 17.0:
                    df_discretized.at[index, col] = 3
                elif row[col] >= 17.0:
                    df_discretized.at[index, col] = 4
            elif col == 'plas':
                if row[col] >= 0 and row[col] < 66.33333333:
                    df_discretized.at[index, col] = 1
                elif row[col] >= 66.33333333 and row[col] < 132.66666667:
                    df_discretized.at[index, col] = 2
                elif row[col] >= 132.66666667 and row[col] < 199.0:
                    df_discretized.at[index, col] = 3
                elif row[col] >= 199.0:
                    df_discretized.at[index, col] = 4
            elif col == 'pres':
                if row[col] >= 0 and row[col] < 40.66666667:
                    df_discretized.at[index, col] = 1
                elif row[col] >= 40.66666667 and row[col] < 81.33333333:
                    df_discretized.at[index, col] = 2
                elif row[col] >= 81.33333333 and row[col] < 122.0:
                    df_discretized.at[index, col] = 3
                elif row[col] >= 122.0:
                    df_discretized.at[index, col] = 4
            elif col == 'skin':
                if row[col] >= 0 and row[col] < 33.0:
                    df_discretized.at[index, col] = 1
                elif row[col] >= 33.0 and row[col] < 66.0:
                    df_discretized.at[index, col] = 2
                elif row[col] >= 66.0 and row[col] < 99.0:
                    df_discretized.at[index, col] = 3
                elif row[col] >= 99.0:
                    df_discretized.at[index, col] = 4
            elif col == 'insu':
                if row[col] >= 0 and row[col] < 282.0:
                    df_discretized.at[index, col] = 1
                elif row[col] >= 282.0 and row[col] < 564.0:
                    df_discretized.at[index, col] = 2
                elif row[col] >= 564.0 and row[col] < 846.0:
                    df_discretized.at[index, col] = 3
                elif row[col] >= 846.0:
                    df_discretized.at[index, col] = 4
            elif col == 'mass':
                if row[col] >= 0 and row[col] < 22.36666667:
                    df_discretized.at[index, col] = 1
                elif row[col] >= 22.36666667 and row[col] < 44.73333333:
                    df_discretized.at[index, col] = 2
                elif row[col] >= 44.73333333 and row[col] < 67.1:
                    df_discretized.at[index, col] = 3
                elif row[col] >= 67.1:
                    df_discretized.at[index, col] = 4
            elif col == 'pedi':
                if row[col] >= 0.078 and row[col] < 0.85866667:
                    df_discretized.at[index, col] = 1
                elif row[col] >= 0.85866667 and row[col] < 1.63933333:
                    df_discretized.at[index, col] = 2
                elif row[col] >= 1.63933333 and row[col] < 2.42:
                    df_discretized.at[index, col] = 3
                elif row[col] >= 2.42:
                    df_discretized.at[index, col] = 4
            elif col == 'age':
                if row[col] >= 21 and row[col] < 41:
                    df_discretized.at[index, col] = 1
                elif row[col] >= 41 and row[col] < 61:
                    df_discretized.at[index, col] = 2
                elif row[col] >= 61 and row[col] < 81:
                    df_discretized.at[index, col] = 3
                elif row[col] >= 81:
                    df_discretized.at[index, col] = 4

# convert every column data type to int

for col in df:   
    if col == 'class':
        continue
    df_discretized[col] = df_discretized[col].astype(int)


# save the discretized dataframe to a csv file called "diabetesTrain_discretized.csv"


df_discretized.to_csv('Parcial_1\\assets\\diabetesTest_discretized.csv', index=False)




