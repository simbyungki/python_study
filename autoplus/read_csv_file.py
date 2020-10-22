import pandas as pd

# csv 파일 로드 > encoding > EUC-KR / CP949
# data = pd.read_csv('C:/Users/PC/Documents/simbyungki/git/python_study/autoplus/csv_file_sample.csv', encoding='CP949')

# 구분이 콤마가 아닌 경우 (Tab, 공백 가능)
# 탭 
# data = pd.read_csv('C:/Users/PC/Documents/simbyungki/git/python_study/autoplus/csv_file_sample.csv', encoding='CP949', delimiter='\t')
# 공백
# data = pd.read_csv('C:/Users/PC/Documents/simbyungki/git/python_study/autoplus/csv_file_sample.csv', encoding='CP949', delimiter=' ')

# 컬럼명이 없는 경우
data = pd.read_csv('C:/Users/PC/Documents/simbyungki/git/python_study/autoplus/csv_file_sample_no_column_name.csv', encoding='CP949', names=['넘버', '대리점', '금월매출', '총 판매수량'])
print(data)
# NaN 데이터가 있는 row 삭제
data = data.dropna(subset=['넘버'])
print(data)