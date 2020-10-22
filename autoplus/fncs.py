# import pandas as pd
# import numpy as np 

# # 데이터 생성
# data = [
# 	[1.4, np.nan],
# 	[7.1, -4.5],
# 	[np.nan, np.nan],
# 	[0.75, -1.3]
# ]
# df = pd.DataFrame(data, columns=['one', 'two'], index=['a', 'b', 'c', 'd'])
# # column 전체 합
# print('<< column 전체 합 >>')
# print(df.sum(axis=0))
# # row 전체 합
# print('<< row 전체 합 >>')
# print(df.sum(axis=1))