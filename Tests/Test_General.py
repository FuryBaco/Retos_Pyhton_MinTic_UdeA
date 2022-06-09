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
#create a copy of data
data_copy = data.copy()
#create a new column called above_avg_temp
data_copy['above_avg_temp'] = data_copy['temperature'].apply(lambda x: 'SI' if x > avg_temp else 'NO' if x < avg_temp else 'IGUAL')
#count the number of times above_avg_temp is SI
count_above_avg_temp_si = data_copy['above_avg_temp'].value_counts()['SI']
#count the number of times above_avg_temp is NO
count_above_avg_temp_no = data_copy['above_avg_temp'].value_counts()['NO']
#count the number of times above_avg_temp is IGUAL if it IGUAL exists
count_above_avg_temp_igual = data_copy['above_avg_temp'].value_counts()['IGUAL'] if 'IGUAL' in data_copy['above_avg_temp'].value_counts() else 0
#make a function that returns the number of times above_avg_temp is SI, NO and IGUAL and check if it exists
def count_above_avg_temp(data_copy):
    count_above_avg_temp_si = data_copy['above_avg_temp'].value_counts()['SI']
    count_above_avg_temp_no = data_copy['above_avg_temp'].value_counts()['NO']
    count_above_avg_temp_igual = data_copy['above_avg_temp'].value_counts()['IGUAL'] if 'IGUAL' in data_copy['above_avg_temp'].value_counts() else 0
    return count_above_avg_temp_si, count_above_avg_temp_no, count_above_avg_temp_igual
#print the count of above_avg_temp
print(count_above_avg_temp_si,count_above_avg_temp_no,count_above_avg_temp_igual)
#convert data_copy to csv
data_copy.to_csv('data_nuevo.csv', index=False)








