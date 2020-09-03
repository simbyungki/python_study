""" 
[2020.09.03]
퀴즈 1. 
1. 극장 좌석 예약 프로그램 > A,B,C,D,E ... 좌석 열을 만드는 함수가 있다. (각 열당 좌석번호는 20번까지 존재)
  ex ) A1, A2, A3, A4 ...
2. 코로나 예방을 위해 한자리씩 여백을 두고 예약가능한 좌석을 만들어야 한다. 
  ex ) A1, A3, A5, A7 ...
"""
# 예약 가능한 좌석 만드는 함수
def make_sheet_row(alphabet, type = 'normal') :
    result_sheets = []
    if type == 'odd' :
        # 홀수 좌석 번호만 예약 가능한 상태로 좌석 list return
        for i in range(1, 21, 2) :
            result_sheets.append(alphabet + str(i))
    elif type == 'even' :
        # 짝수 좌석 번호만 예약 가능한 상태로 좌석 list return
        for i in range(2, 21, 2) :
            result_sheets.append(alphabet + str(i))
    else :
        # 전체 좌석 번호 예약 가능한 상태로 좌석 list return
        for i in range(1, 21) :
            result_sheets.append(alphabet + str(i))
    return result_sheets


# A열 좌석을 만들고, 특이사항 없으므로 열 값만 전달
print(make_sheet_row('A'))
# 결과
# ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17', 'A18', 'A19', 'A20']


# A, B, C, D열 좌석을 만들되, 코로나 예방을 위한 한자리씩 비워 예약 가능토록
# 각 열마다 교차로 홀(odd) / 짝(even) 전달
print(make_sheet_row('A', 'even'))
print(make_sheet_row('B', 'odd'))
print(make_sheet_row('C', 'even'))
print(make_sheet_row('D', 'odd'))
# 결과
# ['A2', 'A4', 'A6', 'A8', 'A10', 'A12', 'A14', 'A16', 'A18', 'A20']
# ['B1', 'B3', 'B5', 'B7', 'B9', 'B11', 'B13', 'B15', 'B17', 'B19']
# ['C2', 'C4', 'C6', 'C8', 'C10', 'C12', 'C14', 'C16', 'C18', 'C20']
# ['D1', 'D3', 'D5', 'D7', 'D9', 'D11', 'D13', 'D15', 'D17', 'D19']