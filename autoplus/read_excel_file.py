# pandas module import
import pandas as pd

# pandas의 read_excel메소드를 사용하고 인자값으로 파일명(경로)와 sheet name이 필요하다.
data = pd.read_excel('C:/Users/PC/Documents/simbyungki/git/python_study/autoplus/excel_file_sample.xlsx', sheet_name='sample')

# 전체출력
# print(data)

# 특정 컬럼만 출력하기 print(data['컬럼명'])
# print(data['대리점'])

# 데이터 활용하여 새로운 컬럼 추가 ((ex) 대리점별 전월과 금월 매출 비교)
# data['전월금월비교'] = data['금월'] - data['전월']

# 판매수량 순 정렬 > ascending=[False] (내림차순)
# data = data.sort_values(by=['총 판매수량'], ascending=[False])

# row 삭제
# data = data.drop([0])

# column 삭제
# del data['TEAM']

# '대리점' 명이 '제주서귀포시대리점'인 row만 출력
# print(data[data['대리점']=='제주서귀포시대리점'])

# '총 판매수량'이 200대 이상인 대리점만 출력
# print(data[data['총 판매수량']>=200])

# 두가지 조건 동시 출력
# print(data[(data['대리점'] == '제주서귀포시대리점') | (data['대리점'] == '강원포천대리점')])

# sort 후 index 새롭게 추가
# data = data.sort_values(by=['총 판매수량'], ascending=[False])
# data = data.reset_index()
# print(data)

# column을 index로 활용하기
data = data.set_index('대리점')
print(data)

# data.to_excel('C:/Users/PC/Documents/simbyungki/git/python_study/autoplus/result.xlsx', sheet_name='result')