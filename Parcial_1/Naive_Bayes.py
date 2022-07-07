# this program is a naive bayes classifier
from email import header
import pandas as pd
from requests import head
# import scikit_learn as sk

# Not mutable variable
# Documentation: \assets\heart-disease.names
# DATA_PATH = 'Parcial_1\\assets\\diabetes.csv'
DATA_PATH = 'assets\\diabetesTest.csv'

# data to classify
data = pd.read_csv(DATA_PATH, header=0)
claz = data.columns[data.shape[1]-1].__str__()
# print(claz)

prior = data.groupby(claz).size().div(len(data)) #count()['Age']/len(data)
print (prior)

# storing headers in a new panda series with the name of the column of df and store each unique value in it
headers = pd.Series(data.columns.values, name='headers')    

Ps = {}


for i in range(len(headers)-1):
    Ps[headers[i]] = data.groupby([claz, data.columns[i].__str__()]).size().div(len(data)).div(prior)

print(Ps)





