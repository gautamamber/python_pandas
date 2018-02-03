#series one dimension like list, string.
import pandas as pd
s = pd.Series([10,20,"mark","john","12.2"])
s1 = pd.Series([12,30,"joe","bob","12.12"])
s4 = pd.Series([10,20,30,40])

d = {'goa' : 10000, 'delhi' : 20000 , 'mumbai' : 10000} #dictionaries

s2 = pd.Series(d)

cities = {'tokyo' : 10000, 'london' : 20000 , 'new-york' : 30000} #dictionaries

cities1 = cities <20000
 
math_func = s4/10

s3 = pd.Series(cities) #return boolean value

print(s2)
print(s)
print(s1)
print(s3)
print(cities1)

s3 = cities['tokyo'] = 50000
print(s3) # cities updated

print('goa' in d) #return boolean
print(math_func)  #mathematical operation result
# use indexing: s[0]
#s[1] 