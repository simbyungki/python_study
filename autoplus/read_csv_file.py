import pandas as pd
import csv
import urllib

# csv 파일 로드 > encoding > EUC-KR / CP949
# data = pd.read_csv('C:/Users/PC/Documents/simbyungki/git/python_study/autoplus/csv_file_sample.csv', encoding='CP949')

# 구분이 콤마가 아닌 경우 (Tab, 공백 가능)
# 탭 
# data = pd.read_csv('C:/Users/PC/Documents/simbyungki/git/python_study/autoplus/csv_file_sample.csv', encoding='CP949', delimiter='\t')
# 공백
# data = pd.read_csv('C:/Users/PC/Documents/simbyungki/git/python_study/autoplus/csv_file_sample.csv', encoding='CP949', delimiter=' ')

data = pd.read_csv('C:/Users/PC/Documents/simbyungki/git/python_study/autoplus/GoXPbGQl-uQ.csv', encoding='CP949')

f = open('C:/Users/PC/Documents/simbyungki/git/python_study/autoplus/GoXPbGQl-uQ.csv', 'r')
rdr = csv.reader(f)

for line in rdr :
	pass
	# print(parse.unquote(line[0]))

print(urllib.parse.unquote_plus('%u548C%uC218%uC5F0', encoding='utf-8', errors='replace'))

f.close()

# 데이터 쓰기
# data['kor'] = []