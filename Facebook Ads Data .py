#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file into DataFrame - Załaduj plik CSV do DataFrame
file_path = r"C:\Users\Acer\Desktop\DA\PYTHON\ZADANIE_2\facebook_ads_data.csv"
df = pd.read_csv(file_path)

# Display first few rows - Sprawdź pierwsze kilka wierszy DataFrame
print(df.head())

# Convert 'ad_date' to datetime format - Przekształć kolumnę 'ad_date' na format daty
df['ad_date'] = pd.to_datetime(df['ad_date'])


# In[2]:


# Filter data for 2021 - Filtruj dane dla roku 2021
df_2021 = df[df['ad_date'].dt.year == 2021]

# Group by date and aggregate - Pogrupuj dane według dnia
daily_data = df_2021.groupby(df_2021['ad_date'].dt.date).sum()

# Plot daily spend - Utwórz wykres dziennych wydatków na reklamę w 2021 roku
plt.figure(figsize=(12, 6))
plt.plot(daily_data.index, daily_data['total_spend'], label='Daily Spend')
plt.xlabel('Date')
plt.ylabel('Total Spend')
plt.title('Daily Advertising Spend in 2021')
plt.legend()
plt.grid(True)
plt.show()

# Plot daily ROMI - Utwórz wykres dziennego ROMI w 2021 roku
plt.figure(figsize=(12, 6))
plt.plot(daily_data.index, daily_data['romi'], label='Daily ROMI', color='orange')
plt.xlabel('Date')
plt.ylabel('ROMI')
plt.title('Daily ROMI in 2021')
plt.legend()
plt.grid(True)
plt.show()


# In[3]:


# Add 7-day rolling average columns - Dodaj kolumny z ruchomą średnią (7 dni) dla total_spend i romi
daily_data['rolling_spend'] = daily_data['total_spend'].rolling(window=7).mean()
daily_data['rolling_romi'] = daily_data['romi'].rolling(window=7).mean()

# Plot 7-day rolling average of spend - Wykres ruchomej średniej kosztów
plt.figure(figsize=(12, 6))
plt.plot(daily_data.index, daily_data['rolling_spend'], label='7-day Rolling Spend')
plt.xlabel('Date')
plt.ylabel('Rolling Spend')
plt.title('7-day Rolling Average of Advertising Spend in 2021')
plt.legend()
plt.grid(True)
plt.show()

# Plot 7-day rolling average of ROMI - Wykres ruchomej średniej ROMI
plt.figure(figsize=(12, 6))
plt.plot(daily_data.index, daily_data['rolling_romi'], label='7-day Rolling ROMI', color='orange')
plt.xlabel('Date')
plt.ylabel('Rolling ROMI')
plt.title('7-day Rolling Average of ROMI in 2021')
plt.legend()
plt.grid(True)
plt.show()


# In[4]:


# Group by campaign name - Pogrupuj dane według nazwy kampanii
campaign_data = df.groupby('campaign_name').sum()

# Plot total spend by campaign - Wykres całkowitych wydatków na reklamę w każdej z kampanii
plt.figure(figsize=(12, 6))
campaign_data['total_spend'].plot(kind='bar')
plt.xlabel('Campaign Name')
plt.ylabel('Total Spend')
plt.title('Total Advertising Spend by Campaign')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Plot total ROMI by campaign - Wykres całkowitego ROMI w każdej z kampanii
plt.figure(figsize=(12, 6))
campaign_data['romi'].plot(kind='bar', color='orange')
plt.xlabel('Campaign Name')
plt.ylabel('Total ROMI')
plt.title('Total ROMI by Campaign')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# In[6]:


# Box plot of daily ROMI distribution by campaign - Box plot dziennego rozkładu wskaźnika ROMI w każdej kampanii
plt.figure(figsize=(12, 6))
sns.boxplot(x='campaign_name', y='romi', data=df)
plt.xlabel('Campaign Name')
plt.ylabel('ROMI')
plt.title('Daily ROMI Distribution by Campaign')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# In[7]:


# Histogram of ROMI values - Histogram z rozkładem wartości ROMI
plt.figure(figsize=(12, 6))
sns.histplot(df['romi'], bins=20, kde=True)
plt.xlabel('ROMI')
plt.title('Distribution of ROMI Values')
plt.grid(True)
plt.show()


# In[8]:


# Correlation heatmap - Mapa cieplna korelacji
plt.figure(figsize=(12, 6))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')
plt.show()

# Print correlations for 'total_value' - Sprawdź korelacje dla kolumny 'total_value'
total_value_corr = correlation_matrix['total_value'].sort_values()
print(total_value_corr)


# In[9]:


# Scatter plot with linear regression - Wykres punktowy z regresją liniową
plt.figure(figsize=(12, 6))
sns.lmplot(x='total_spend', y='total_value', data=df, height=6, aspect=1.5)
plt.xlabel('Total Spend')
plt.ylabel('Total Value')
plt.title('Linear Regression: Total Spend vs Total Value')
plt.grid(True)
plt.show()


# In[ ]:




