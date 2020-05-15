import random
import pandas as pd


##TODO: Randomly choose the data 66% of weightage to GOOD and 33% to bad
options=['GOOD', 'GOOD', 'BAD']

##TODO: Create the data for the month of Nov-Dec , hourly basis
datelist=pd.date_range(start='2018-11-01 00:00:00', end='2018-12-31 00:00:00', freq='H')

#TODO:Create the unique Unit_ID for all the files
x=random.sample(range(1, 1442), 1441)

##TODO: Create the string, write and save the text file
pickfiles='F091-'
print('here')
for i in range(1440):
    string='1 '+random.choice(options)+' SIN'+'\n   RESPONSE '+random.choice(options)+'\n   Polarity '+random.choice(options)+'\n   RUB+BUZZ '+random.choice(options)+'\n   THD '+random.choice(options)+'\n'+str(datelist[i])+'\nUNIT N. F091-0'+str(x[i])+random.choice(options)
    f= open((pickfiles+str(x[i])+'.txt'),"w+")
    
    f.write(string)
    f.close