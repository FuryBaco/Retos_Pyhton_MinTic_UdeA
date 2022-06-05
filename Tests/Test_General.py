#open data.csv and convert to dataframe
import pandas as pd
import numpy as np
data = pd.read_csv('data.csv')
#calculate the average of temperature and pressure 
avg_temp = data['temperature'].mean()
avg_pressure = data['pressure'].mean()
#calculate the standard deviation of temperature and pressure
std_temp = data['temperature'].std()
std_pressure = data['pressure'].std()
#calculate the minimum and maximum of temperature and pressure
min_temp = data['temperature'].min()
max_temp = data['temperature'].max()
#cacluta mean of temperature and pressure based on location
avg_temp_press_loc = data.groupby('location')['temperature','pressure'].mean()
#convert avg_temp_press_loc to dictionary
avg_temp_press_loc_dict = avg_temp_press_loc.to_dict()
#print the dictionary
print(avg_temp_press_loc_dict)
#format the dictionary VALUES to 2 decimal places









