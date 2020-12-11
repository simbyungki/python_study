from openpyxl import Workbook

# 워크북 생성
wb = Workbook()
# 활성화된 sheet 가져옴
ws = wb.active
# 시트 이름 변경
ws.title = 'BK_Sheet'
# 저장
wb.save('C:/Users/PC/Documents/simbyungki/git/python_study/rpa/excel/sample.xlsx')
# 닫기
wb.close