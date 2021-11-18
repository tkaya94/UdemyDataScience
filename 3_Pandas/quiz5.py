import pandas as pd
 
df1 = pd.DataFrame({
    'student_id': ['S1', 'S2', 'S3'],
    'name': ['Jan', 'Christian', 'Marius'],
    'marks': [100, 90, 80]
})
 
df2 = pd.DataFrame({
    'student_id': ['S4', 'S5', 'S6'],
    'name': ['Marco', 'Anne', 'Dennis'],
    'marks': [95, 100, 90]
})
 
print(df1)
print(df2)
print(pd.concat([df1, df2], axis=1))