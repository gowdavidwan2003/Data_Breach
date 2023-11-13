#!/usr/bin/env python
# coding: utf-8

# ## Importing Libraries

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# ## Reading data 

# In[2]:


df = pd.read_csv('DataBreaches.csv')


# ## Understanding Data

# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.loc[120,'Year'] = 2014
df.loc[78,'Year'] = 2018


# ## Companies with greatest number of attacks
# 

# In[8]:


companydf = df.groupby('Entity')


# In[9]:


companydf.sum().sort_values('Records',ascending=False).head(5)


# In[10]:


companydf.sum().sort_values('Records').head(5)


# # The most number of data breaches has occurred because of the YAHOO

# In[ ]:





# ## Breaches based on Organisation type

# In[11]:


orgdf = df.groupby('Organization type')


# In[12]:


orgdf.sum().sort_values('Records',ascending=False).head(5)


# In[13]:


orgdf.sum().sort_values('Records').head(5)


# In[14]:


total_financial = 885000000+818597083
total_financial


# # Web is the most prone type for the Data Breaches and the least prone are Advertaising

# Following web, the high incidence of data breaches in the financial sector highlights the urgent need to strengthen our banking and financial services data systems. As digital transactions become more prevalent, ensuring system security is crucial. This involves not only safeguarding financial assets but also maintaining user trust. Investments in advanced cybersecurity, adherence to data management best practices, and compliance with data protection regulations are key. Promoting security awareness and advocating for stricter data breach legislation can further bolster defenses, helping to reduce data breach risks and enhance system integrity.

# In[15]:


methoddf = df.groupby('Method')


# In[16]:


methoddf.sum().sort_values('Records',ascending=False).head(5)


# In[17]:


methoddf.sum().sort_values('Records').head(5)


# ## The most common and widely used method for data breaches are Hacking followed by poor security

# The fact that the third most common source of data breaches is unidentified presents a significant concern. It’s crucial to promptly discern and address this unknown element to bolster our data security measures. By doing so, we can potentially mitigate further data breaches. Additionally, this situation underscores the importance of investing in advanced threat detection systems and promoting a culture of security awareness within organizations

# In[18]:


df.Year = pd.DatetimeIndex(df.Year).year


# In[19]:


year1df = df.groupby('Year')
yeardf = year1df.sum()


# In[20]:


yeardf = yeardf[1:]
yeardf


# In[21]:


yeardf.sort_values('Records',ascending=False).head(5)


# In[22]:


yeardf.sort_values('Records').head(5)


# In[23]:


sns.set_style('darkgrid')
plt.xticks([2004,2006,2008,2010,2012,2014,2016,2018,2020,2022])
plt.plot(yeardf.index,yeardf.Records, '*-r');



# ## The Data Breaches is maximum in year 2013 and 2019 

# The decrease in data breaches in 2020 was less when compared to 2019. This might be because the new data generated in 2020 is far more less than the data generated in 2020 since there was lockdown in 2020. This might be the reason since many businesses and institutions were operating remotely or even shut down for a period of time, leading to a decrease in the overall data flow. Additionally, enhanced security measures might have been implemented as organizations adapted to remote work, further contributing to the decrease in data breaches. However, it’s important to note that these are just potential factors, and the actual reasons could vary widely based on individual circumstances.

# In[24]:


df2013 = df[df['Year']==2013]
df2013.sort_values('Records',ascending=False)


# In[25]:


df.loc[283,'Records']/df2013['Records'].sum()*100


# ## Observation for Spike in 2013

# Indeed, the massive data breach at Yahoo in 2013 significantly contributed to the spike in data breaches that year. The breach, which affected billions of user accounts, accounted for a staggering 86.5% of all data breaches in 2013. This incident underscores the importance of robust cybersecurity measures and the potential scale of damage that can occur when these measures fail. It serves as a stark reminder for all organizations to continually review and enhance their data security protocols to protect against such incidents.

# In[26]:


df2019 = df[df['Year']==2019]
sorted1 = df2019.sort_values('Records',ascending=False)
sorted1


# In[27]:


sorted1.head(14)['Records'].sum()/df2019['Records'].sum()*100


# ## Observation for Spike in 2019

# Indeed, 2019 was a significant year for data breaches, with many major companies falling victim due to inadequate security measures. A total of 24 major data breaches were recorded, each involving the leak of over 100 million records. These breaches collectively accounted for a staggering 98.5% of all leaked data that year. This highlights the critical importance of robust cybersecurity measures and the potential scale of damage that can occur when these measures are not adequately implemented or maintained. It serves as a stark reminder for all organizations to continually review and enhance their data security protocols to protect against such incidents

# In[ ]:




