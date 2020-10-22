import pandas as pd
import numpy as np

# # Series 정의
# obj = pd.Series([4, 6, -2, 5])
# print('<Series 정의>')
# print(obj)

# # Series의 index만 확인
# print('Series의 index만 >> ', obj.index)

# # Series의 값만 확인
# print('Series의 값만 >> ', obj.values)

# # Series의 자료형 확인
# print('Series의 자료형 >> ', obj.dtypes)

# # Python의 Dictionary 자료형을 Series data로 변경
# # Dictionary의 Key가 Series의 index가 된다.
# data = {'Kim':35000, 'Sim':40000, 'Jung':20000, 'Park':40200}
# obj = pd.Series(data, name='직원별 인센티브 현황')
# print(obj)


# Data Frame 정의
# data는 Python의 Dictonary로 정의할 수 있다.
# data = {
# 	'name': ['Beomwoo', 'Beomwoo', 'Beomwoo', 'Kim', 'Park'],
# 	'year': [2013, 2014, 2015, 2016, 2015],
# 	'points': [1.5, 1.7, 3.6, 2.4, 2.9]
# }
# obj = pd.DataFrame(data)
# print(obj)

# # 계산 가능한 다양한 결과값 제공
# print(obj.describe())

# # 특정 coulmn만 보기
# print(obj[['year', 'points']])

# # coulmn 추가 및 값 대입
# obj['age'] = [23, 34, 55, 23, 44]
# print(obj)

# # 순서대로 증가하는 숫자 column 추가
# obj['new_index'] = np.arange(len(obj.index-1))
# print(obj)

# Series 데이터 > Data Frame에 추가
# sdata = [23000, 43000, 42000, 44000]
# ss = pd.Series(sdata, index=[0, 2, 3, 4], name='직원별 인센티브 현황')
# obj['incentive'] = ss
# obj = obj.dropna(subset=['incentive'])
# print(obj)

# 'points'값이 2.0이 넘는지 체크하여 새로운 column 'success'에 boolean값으로 표시
# obj['success'] = obj['points'] > 2.0
# print(obj)

# points, new_index값은 필요 없으므로 삭제 (column삭제)
# del obj['points']
# del obj['new_index']
# print(obj)

# row 선택 (0~2번째 index에 해당하는 row)
# print(obj[0:3])

# loc 메소드 사용하여 row 선택 > 반환형태는 Series
# print(obj.loc[0])

# loc 메소드 사용하여 row 선택 후 특정 column값만 반환 > Series
# 0부터 2까지의 index 선택 후 'success' 값 반환
# print(obj.loc[0:3, 'success']) 
# print(obj.loc[0:3, ['name', 'success']])

# loc(iloc) 메소드 > 새로운 행 삽입
# obj.loc[5, :] = ['Sim', 2018, 45000, False]
# print(obj)

# boolean indexing
# print(obj['year'] > 2014)
# 2014년보다 큰 row 전부 출력
# print(obj.loc[obj['year']>2014 , :])

# 'name'이 'Park'인 row의 'name'과 'incentive'값을 반환
# print(obj.loc[obj['name'] == 'Park', ['name', 'incentive']])

# 논리 연산 'year'가 2014보다 크면서 'incentive'가 42000보다 큰 row 반환
# print(obj.loc[(obj['year'] > 2014) & (obj['incentive'] > 42000), :])


