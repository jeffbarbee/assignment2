#!/usr/bin/env python
# coding: utf-8

import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

if len(sys.argv) != 4:
    print("Usage: python RegressionPython.py Regression_data.csv YearsExperience Salary")
    sys.exit(1)

filename = sys.argv[1]
x_col = sys.argv[2]
y_col = sys.argv[3]

data = pd.read_csv(filename)
model = LinearRegression()
model.fit(data[[x_col]], data[[y_col]])

plt.scatter(data[[x_col]], data[[y_col]], color='red')
plt.plot(data[[x_col]], model.predict(data[[x_col]]), color='blue')
plt.title(f'{y_col} vs {x_col}')
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.savefig("linear_regression_python_output.png")
plt.show()


# This notebook demonstrates a simple linear regression analysis using [Python/R] to model Salary based on Years of Experience.

# In[1]:


import pandas as pd
dataset = pd.read_csv("regression_data.csv")


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="red")


# In[4]:


from sklearn.linear_model import LinearRegression


# In[5]:


model = LinearRegression()


# In[6]:


model.fit(dataset[["YearsExperience"]], dataset[["Salary"]])


# In[7]:


plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="red")
plt.plot(dataset["YearsExperience"], model.predict(dataset[["YearsExperience"]]), color="blue")
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()


# In[8]:


model.score(dataset[["YearsExperience"]], dataset[["Salary"]])  # R-squared


# In[20]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from sklearn.metrics import mean_squared_error


# # Updated Code

# In[31]:


slope = model.coef_[0][0]
print(slope)
intercept= model.intercept_[0]
print(intercept)


# In[22]:


y_pred = slope * dataset["YearsExperience"] + intercept


# In[23]:


mse = mean_squared_error(dataset["Salary"], y_pred)
print(mse)
r_value = model.score(dataset[["YearsExperience"]], dataset[["Salary"]])
print(r_value)


# In[35]:


plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="red")
plt.plot(dataset["YearsExperience"], model.predict(dataset[["YearsExperience"]]), color="blue")
#plt.text(1.5, max(dataset["Salary"]) - 1,
 #   f"y = {slope:.2f}x + {intercept:.2f}\n"
  #  f"r = {r_value:.2f}\nMSE = {mse:.2f}",
   # fontsize=12)
plt.text(1.5, 60000, f"y = {slope:.2f}x + {intercept:.2f}\nr = {r_value:.2f}\nMSE = {mse:.2f}")
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()


# In[ ]:




