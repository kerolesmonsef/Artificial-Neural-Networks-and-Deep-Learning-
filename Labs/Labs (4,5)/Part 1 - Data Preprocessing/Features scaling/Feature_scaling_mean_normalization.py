# Data Preprocessing

# Importing the libraries
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Dataset_3.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

# Feature scaling: mean normalization
from sklearn.preprocessing import Normalizer
# Here we scale all input features 
normailzation = Normalizer()
X_scaled = normailzation.fit_transform(X)



