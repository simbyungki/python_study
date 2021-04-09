import pandas as pd
import csv
import urllib.parse

# csv 파일 로드 > encoding > EUC-KR / CP949
# data = pd.read_csv('C:/Users/PC/Documents/simbyungki/git/python_study/autoplus/csv_file_sample.csv', encoding='CP949')

# 구분이 콤마가 아닌 경우 (Tab, 공백 가능)
# 탭 
# data = pd.read_csv('C:/Users/PC/Documents/simbyungki/git/python_study/autoplus/csv_file_sample.csv', encoding='CP949', delimiter='\t')
# 공백
# data = pd.read_csv('C:/Users/PC/Documents/simbyungki/git/python_study/autoplus/csv_file_sample.csv', encoding='CP949', delimiter=' ')

data = pd.read_csv('C:/Users/PC/Documents/simbyungki/git/python_study/autoplus/GoXPbGQl-uQ.csv', encoding='utf-8')

f = open('C:/Users/PC/Documents/simbyungki/git/python_study/autoplus/GoXPbGQl-uQ.csv', 'r', encoding='latin')
rdr = csv.reader(f)

result_list = []
for idx, line in enumerate(rdr) :
	if idx == 4 :
		break
	elif idx == 0 :
		continue
	else : 
		print(idx)
		print(type(line[0]))
		print(line[0])
		st = line[0].encode('utf-8')
		print(st)
		print(st.decode('utf-8'))


st = '\u6587 \uB300\uD1B5\uB839 \uC9C0\uC9C0\uC728 34%\uB85C \uCDE8\uC784\uD6C4 \uCD5C\uC800\u2026\'\uC11C\uC6B8 \uC9C0\uC9C0\uC728 26%\' \u3161\uC544\uC2DC\uC544\uACBD\uC81C\u3161'.encode('utf-8')
# print(type(st))
# print(st)
# print(st.decode('utf-8'))
# print(urllib.parse.unquote(st))

f.close()

# 데이터 쓰기
# data['kor'] = []