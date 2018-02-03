# csv => comma seperated value 
#example
"""
Date,A,B,C
1234,a,d,g
1255,b,e,h
6789,c,f,i
"""
# now read csv file

import pandas as pd
a = pd.read_csv('amber.csv',names = ['a1','a2','a3','a4'], header = 0) #remove header 
print(a)
