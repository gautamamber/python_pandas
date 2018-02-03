#getting data from large csv file
#  https://grouplens.org/datasets/movielens/

import pandas as pd
user = pd.read_csv('ml-latest/links')
print(user.head()) # it prints first 5 results 
print(user.tail()) #last 5 lines 
print(user.head(2)) #prints first 2 lines
print(user.tail(3)) #last 3 lines
print(user[9:20]) #print data acc to slicing
print(user[10:]) #print 10 to upto last

a = user['imdpId'].head()
print(a) #return only one column

print(user['imdbId'].head(20)) #print first 10 rows of imdbId column

# If want 2 column make an array then fetch
