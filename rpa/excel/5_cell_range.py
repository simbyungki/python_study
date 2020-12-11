from openpyxl import Workbook
from random import *
wb = Workbook()
ws = wb.active
ws.title = '3-A반 성적표'

# 1줄씩 데이터 넣기
ws.append(['번호', '영어', '수학'])

for i in range(1, 11) : # 10개 데이터 넣기
	ws.append([i, randint(0, 100), randint(0, 100)])

col_B = ws['B']
for cell in col_B : 
	print(cell.value)

wb.save('C:/Users/PC/Documents/simbyungki/git/python_study/rpa/excel/sample.xlsx')
wb.close