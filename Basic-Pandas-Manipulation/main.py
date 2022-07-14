#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
# Step 1: Use the appropriate pandas method to read the titanic data into your python file 
titanic_data = pd.read_csv('titanic.csv')
titanic_data


# In[10]:


# Step 2(a): Use the pandas method that reads the first 25 lines of the dataset
first_25_passengers = titanic_data.head(25)
first_25_passengers


# In[12]:


# Step 2(b): Use the pandas method thats reads the last 25 lines of the dataset
last_25_passengers = titanic_data.tail(25)
last_25_passengers


# In[13]:


# Step 3: Use the pandas method that only tells us the number of rows and columns in our data
titanic_shape = titanic_data.shape
titanic_shape


# In[23]:


# Step 4: Describe the titanic data
titanic_description = titanic_data.describe()
titanic_description


# In[22]:


# Step 5(a): How many passengers were between the ages of 0 to 16? 
children = titanic_data[ (titanic_data['Age'] >= 0) & (titanic_data['Age'] <= 16)]
children


# In[26]:


# Step 5(b): How many passengers were between the ages of 17 to 25?
young_adults = titanic_data[ (titanic_data['Age'] >= 17) & (titanic_data['Age'] <= 25)]
young_adults


# In[28]:


# Step 5(c): How many passengers were between the ages of 26 to 40?
adults = titanic_data[ (titanic_data['Age'] >= 26) & (titanic_data['Age'] <= 40) ]
adults


# In[32]:


# Step 5(d): How many passengers were between the ages of 41 to 59?
mature_adults = titanic_data[ (titanic_data['Age'] >= 41) & (titanic_data['Age'] <= 59) ]
mature_adults


# In[33]:


# Step 5(e): How many passengers were 60 or older?
seniors = titanic_data[ titanic_data['Age'] >= 60]
seniors


# In[56]:


# Step 6: How many values are missing from the "age" column
missing_ages = titanic_data.isnull().sum()
missing_ages

# you could also do titanic_data.count()
# or you could do titanic_data['age'].isnull()


# In[60]:


# Step 7: List out all the available passengers' ages
age_list = titanic_data['Age'].dropna().unique()
age_list


# In[63]:


# Step 8: Filter the DataFrame to find all passengers who boarded the Titanic at Port Cherbourg
cherbourg_passengers = titanic_data[titanic_data['Embarked'] == "C"]
cherbourg_passengers


# In[69]:


# Step 9(a): Find the average age of all female passengers
avg_fem_age = titanic_data[ titanic_data['Sex'] == "female"]['Age'].mean()
avg_fem_age


# In[71]:


# Step 9(b): Find the average age of all male passengers
avg_male_age = titanic_data[ titanic_data['Sex'] == "male"]['Age'].mean()
avg_male_age


# In[83]:


# Step 10(a): Find the survival percentage of passengers in group "C"
cherbourg_survival = titanic_data[ (titanic_data['Embarked'] == 'C') & (titanic_data['Survived'] == 1)]
all_cherbourg_passengers = titanic_data[ (titanic_data['Embarked'] == "C")]
len(cherbourg_survival)/len(all_cherbourg_passengers) * 100


# In[97]:


# Step 10(b): Find the survival percentage of passengers in group "Q"
queenstown_survival = titanic_data[ (titanic_data['Embarked'] == 'Q') & (titanic_data['Survived'] == 1)]
all_queenstown_passengers = titanic_data[ (titanic_data['Embarked'] == "Q")]
len(queenstown_survival)/len(all_queenstown_passengers) * 100


# In[98]:


# Step 10(c): Find the survival percentage of passengers in group "S"
south_survival = titanic_data[ (titanic_data['Embarked'] == 'S') & (titanic_data['Survived'] == 1)]
all_southampton_passengers = titanic_data[ (titanic_data['Embarked'] == "S")]
len(south_survival)/len(all_southampton_passengers) * 100


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




