import pandas as pd
import numpy as np 


# Data Frame 생성 (random) 
# index와 coulmn을 설정하지 않으면 기본값으로 0부터 시작하는 정수형 숫자로 입력된다.
df = pd.DataFrame(np.random.randn(6,4))
# print(df)

# column 네임 추가
df.columns = ['A', 'B', 'C', 'D']
# index 네임 추가 > date_range 메소드 
df.index = pd.date_range('20201019', periods=6)

# column 추가 > NaN
df['E'] = [1.0, np.nan, 3.5, 6.1, np.nan, 7.0]
# print(df)

# row삭제
df.drop(pd.to_datetime('2020-10-22'))
print(df)