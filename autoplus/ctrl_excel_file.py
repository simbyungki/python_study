import pandas as pd

data = pd.read_excel('C:/Users/PC/Documents/simbyungki/git/python_study/autoplus/excel_file_sample.xlsx', sheet_name='sample')
print(data[['차량명', '주행거리']])