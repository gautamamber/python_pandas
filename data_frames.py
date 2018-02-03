# Tbular data structures, rows and columns, excel sheets.
import pandas as pd
data = { 'students': ["mark","bob","joe","steven"],
'English': [80,90,88,70],
'Social': [50,60,70,66],
'sports': ["cricket","yoga","golf","basket-ball"]
} # 2D data in the form of dictionary

students = pd.DataFrame(data, columns = ["students" , "English", "Social", "sports"])
print(students)
